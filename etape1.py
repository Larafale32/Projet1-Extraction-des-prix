import requests
from bs4 import BeautifulSoup
import csv
import os

# URL de la page du livre dont je souhaite récup les infos
from fonctions import find_product, save_to_csv

# URL du produit à analyser
url = 'http://books.toscrape.com/catalogue/the-murder-of-roger-ackroyd-hercule-poirot-4_852/index.html'

# Récupérer les informations du produit
List = find_product(url)

# Afficher les données récupérées
print(List)

# Sauvegarder les données dans un fichier CSV
csv_filename = "info_livre.csv"
save_to_csv(csv_filename, List)