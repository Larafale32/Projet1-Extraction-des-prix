import requests
from bs4 import BeautifulSoup
import csv
import os


def find_product(url):

    #Récupère les informations d'un produit à partir de son URL.
    #Renvoie une liste contenant les informations extraites.

    response = requests.get(url)
    List = []

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        product = soup.find("article", class_='product_pod')

        if product:  # Si un produit est trouvé
            img = product.find('img')
            image = img['src'] if img else None  # Récupérer l'image ou None si absente

            title_tag = product.find('h3').find('a')
            title = title_tag.get_text()  # Récupérer le titre

            price_tag = product.find(class_='price_color')
            price = price_tag.get_text()  # Récupérer le prix

            List.append((image, title, price))  # Ajouter les infos à la liste

    return List


def save_to_csv(filename, data):

    #Enregistre les données dans un fichier CSV et l'ouvre.

    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Image', 'Title', 'Price'])  # En-têtes du fichier
        writer.writerows(data)  # Données extraites

    os.system(f"open {filename}")  # Ouvrir le fichier (fonctionne sur macOS)

