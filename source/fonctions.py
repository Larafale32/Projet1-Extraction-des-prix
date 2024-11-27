import csv
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def save_to_csv(filename, data):
    """Sauvegarde les données dans un fichier CSV."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Écrire les en-têtes des colonnes
        writer.writerow(["Numéro", "Image", "Titre", "Prix"])
        # Ajouter un compteur pour la numérotation des livres
        for index, row in enumerate(data, start=1):
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
        price = (
            soup.find("p", class_="price_color").get_text()
            if soup.find("p", class_="price_color")
            else ""
        )
        return [image_url, title, price]

    return []


def find_books(base_url, category, num_pages=3):
    """Récupère les informations des livres d'une catégorie spécifique."""
    all_data = []

    category_url = urljoin(base_url, category)

    if num_pages > 1:
        for i in range(num_pages):
            # Créer une URL pour accéder à une page spécifique de la liste des livres
            page_url = category_url + "/page-" + str(i+1) +".html"
            print("Accès à la page " + page_url)
            response = requests.get(page_url)

            if response.ok:
                soup = BeautifulSoup(response.text, "html.parser")
                books = soup.find("ol", class_="row")
                if books:
                    books = books.find_all(
                        "li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"
                    )

                    for book in books:
                        product_url = urljoin(base_url + "catalogue/", book.find("a")["href"])
                        # Appel de `find_book` pour chaque livre
                        book_data = find_book(product_url)
                        if book_data:
                            all_data.append(book_data)


    else:
            page_url = category_url + "/index.html"
            print("Accès à la page " + page_url)

            response = requests.get(page_url)

            if response.ok:
                soup = BeautifulSoup(response.text, "html.parser")
                books = soup.find("ol", class_="row")
                if books:
                    books = books.find_all(
                        "li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"
                    )

                    for book in books:
                        product_url = urljoin(base_url + "catalogue/", book.find("a")["href"])
                        # Appel de `find_book` pour chaque livre
                        book_data = find_book(product_url)
                        if book_data:
                            all_data.append(book_data)

    # Sauvegarder les données dans un fichier CSV
    save_to_csv("books_info.csv", all_data)
    print("Les données ont été sauvegardées dans 'books_info.csv'.")



def find_all_books(num_pages = 50):
    all_data = []
    category = None
    base_url = "http://books.toscrape.com/catalogue/category/books_1"

    all_data.append(find_books(base_url, category, num_pages))

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
            print(f"Image téléchargée avec succès à l'adresse {file_path}")
    else:
        print(f"Impossible de télécharger l'image à l'URL {url_image}")



