# -*- coding: utf-8 -*-

import csv
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def clean_price(value):
    """Supprime les caractères indésirables dans les prix."""
    return value.replace("Â", "").replace("£", "").strip()

def save_to_csv(filename, data):
    """Sauvegarde les données dans un fichier CSV."""
    data_folder = '/Users/arnauddekertanguy/Documents/openclassrooms/Projets-Soutenance/Porjet1-Prg-Extraction-des-prix/data'

    # Créer le dossier 'data' s'il n'existe pas
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Construire le chemin complet du fichier CSV
    file_path = os.path.join(data_folder, filename)
    # Créer le dossier s'il n'existe pas
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Écrire les en-têtes des colonnes
        writer.writerow(["Numéro", "Image", "Titre", "Prix", "in_stock", "star", "upc",
                         "product_type", "price_without_tx", "price_with_tx", "tx", "review"])

        # Ajouter un compteur pour la numérotation des livres
        for index, row in enumerate(data, start=1):
            # Nettoyer les prix dans les colonnes nécessaires
            row[2] = clean_price(row[2])  # Prix principal
            row[7] = clean_price(row[7])  # Prix sans taxe
            row[8] = clean_price(row[8])  # Prix avec taxe
            row[9] = clean_price(row[9])  # Taxe

            # Écrire la ligne nettoyée
            writer.writerow([index] + row)

    os.system(f"open {filename}")


def find_book(url):
    """Récupère les informations d'un livre à partir de son URL."""
    info_livre = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")

        # Récupérer l'image du livre (convertir en URL absolue)
        image_tag = soup.find("img")
        image_url = urljoin(url, image_tag["src"]) if image_tag else ""

        # Récupérer le titre du livre
        title = soup.find("h1").get_text() if soup.find("h1") else ""

        # Récupérer le prix du livre
        price_bis = (
            soup.find("p", class_="price_color").get_text()
            if soup.find("p", class_="price_color")
            else ""
        )
        price = clean_price(price_bis)

            # Récupérer la disponibilité
        in_stock = soup.find("p", class_="instock availability")
        in_stock = in_stock.get_text().strip().replace("\n", "") if in_stock else ""

        # Récupérer la note du livre
        rating = soup.find("p", class_="star-rating")
        star = ""
        if rating:
            star = rating.get("class")[1] + "/Five"

        # Récupérer les informations produit (UPC, type, prix sans taxes, etc.)
        table = soup.find("table", class_="table table-striped")
        all_tr = table.find_all("tr")
        upc = all_tr[0].find("td").get_text()
        product_type = all_tr[1].find("td").get_text()
        price_without_tx = all_tr[2].find("td").get_text()
        price_without_tx = clean_price(price_without_tx)
        price_with_tx = all_tr[3].find("td").get_text()
        price_with_tx = clean_price(price_with_tx)
        tx = all_tr[4].find("td").get_text()
        review = all_tr[6].find("td").get_text()

        # Ajouter toutes les informations dans info_livre (11 éléments)
        info_livre.append([image_url, title, price, in_stock, star, upc, product_type,
                           price_without_tx, price_with_tx, tx, review])

    return info_livre






def find_books(base_url, category):
    """Récupère les informations des livres d'une catégorie spécifique."""
    all_data = []

    # URL de la catégorie
    category_url = urljoin(base_url, category)
    page_number = 1  # On commence à la première page

    # Boucle pour définir le nombre de pages à scraper
    while True:
        # Construire l'URL de la page actuelle
        page_url = category_url + "/page-" + str(page_number) + ".html" if page_number > 1 else category_url + "/index.html"
        print("Accès à la page :", page_url)

        response = requests.get(page_url)  # Récupérer la page
        if not response.ok:  # Si la page n'est pas trouvée, arrêter
            break

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find("ol", class_="row")  # Trouver les livres sur la page
        if not books:  # Si aucune liste de livres n'est trouvée, arrêter
            print("Aucune donnée trouvée. Fin du scraping.")
            break

        # Traiter les livres trouvés
        for book in books.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
            product_url = urljoin(base_url + "catalogue/", book.find("a")["href"])
            book_data = find_book(product_url)
            if book_data:
                all_data.extend(book_data)

        page_number += 1 # Ajouter 1 à page-number pour passer à la page suivante


    # Sauvegarder les données dans un fichier CSV
    if all_data:
        save_to_csv("books_info.csv", all_data)
        print("Les données ont été sauvegardées dans 'books_info.csv'.")
    else:
        print("Aucune donnée n'a été récupérée.")

    return all_data


def find_all_books():
    all_data = []
    category = None
    base_url = "http://books.toscrape.com/catalogue/category/books_1"

    all_data.append(find_books(base_url, category))

def find_all_images(num_pages = 50):
    all_data = []
    base_url = "http://books.toscrape.com/catalogue/category/books_1"
    for i in range(num_pages):

        url = base_url + "/page-" + str(i + 1) + ".html"
        print("Accès à la page " + url)


        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find("ol", class_="row")

            if books:
                books = books.find_all(
                    "li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"
                )
                for book in books:
                    image_url = book.find("img").get("src")
                    image_url = urljoin(base_url, image_url)
                    all_data.append(image_url)
                    print(len(all_data))

                    download_images(image_url, destination="/Users/arnauddekertanguy/Documents/img_books")




            # Recuupérer l'image du livre (convertir en URL absolue)
                    #image_tag = soup.find("img")
                    #image_url = urljoin(url, image_tag["src"])
                    #all_data.append(image_url)
                    #print(all_data)



def download_images(url_image, destination):
    # créer un dossier s'il n'existe pas
    if not os.path.exists(destination):
        os.makedirs(destination)

    file_name = url_image.split("/")[-1]
    file_path = os.path.join(destination, file_name)

    response = requests.get(url_image)
    if response.ok:
        #chemin complet vers le fichier
        with open(os.path.join(destination, file_name), "wb") as file:
            file.write(response.content)
            print("Image téléchargée avec succès à l'adresse" + str(file_path))
    else:
        print("Impossible de télécharger l'image à l'URL " + url_image)



