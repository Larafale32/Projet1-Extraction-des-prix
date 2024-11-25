import requests
from bs4 import BeautifulSoup
import csv
import os

from fonctions import find_book, save_to_csv

url = "http://books.toscrape.com/catalogue/the-murder-of-roger-ackroyd-hercule-poirot-4_852/index.html"

# Récupérer les informations du produit
book_data = find_book(url)

# Afficher les données récupérées
print("Données récupérées pour le livre :")
print(book_data)

# Sauvegarder les données dans un fichier CSV
csv_filename = "info_livre.csv"
save_to_csv(csv_filename, [book_data])  # Passer book_data comme une liste de liste


# URL de la page du livre dont je souhaite récup les infos
