import requests
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urljoin


def save_to_csv(filename, data):
    """Sauvegarde les données dans un fichier CSV."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Écrire les en-têtes des colonnes
        writer.writerow(["Image", "Titre", "Prix"])
        # Écrire chaque ligne de données
        writer.writerows(data)

    os.system(f"open {filename}")


def find_book(url):
    """Récupère les informations d'un livre à partir de son URL."""
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")

        # Récupérer l'image du livre
        image_url = soup.find("img")["src"] if soup.find("img") else ""

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


def find_books(url):

    # Initialisation de la liste pour stocker les données de tous les livres
    all_data = []

    # Parcours des 25 pages
    for i in range(25):

        # Créer une URL pour accéder à une page spécifique de la liste des livres
        # L'URL de base est complétée par le paramètre "?page=" suivi du numéro de la page.
        # Le "?"  indique le début des paramètres de requête, utilisés pour transmettre des informations
        # supplémentaires au serveur.
        # Par exemple, "?page=2" informe le site que l'on souhaite afficher la deuxième page des livres.
        page_url = url + "?page=" + str(i + 1)

        response = requests.get(page_url)

        if response.ok:  # Vérifier si la requête est valide
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find("ol", class_="row")
            if books:
                books = books.find_all(
                    "li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"
                )

                for book in books:  # Parcours des livres sur la page
                    product_url = urljoin(
                        "http://books.toscrape.com/catalogue/category/books/fantasy_19/",
                        book.find("a")["href"],
                    )
                    # Appel de `find_book` pour chaque livre
                    book_data = find_book(product_url)
                    if book_data:  # Si les données du livre ont été trouvées
                        all_data.append(
                            book_data
                        )  # Ajouter les données à la liste globale
            else:
                break  # Arrêter si aucune liste de livres n'est trouvée sur la page
        else:
            break  # Arrêter en cas de problème de requête

    # Sauvegarder les données dans un fichier CSV une fois que tout est collecté
    save_to_csv("books_info.csv", all_data)
    print("Les données ont été sauvegardées dans 'books_info.csv'.")
