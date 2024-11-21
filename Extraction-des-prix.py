import requests
from bs4 import BeautifulSoup
import csv
import os

# URL de la page du livre dont je souhaite récup les infos
url = 'http://books.toscrape.com/catalogue/the-murder-of-roger-ackroyd-hercule-poirot-4_852/index.html'
response = requests.get(url)

# Liste pour stocker les infos du livre
List = []

# Je vérifie si la requête réussie
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml') # J'utilise BS4 pour analyser le contenu HTML

    # J'utilise une variable product pour trouver la classe product_pod dans les balises article
    product = soup.find("article", class_= 'product_pod')

    if product : #Si product est trouvé alors j'exécute une action
            img = product.find('img') #Je cherche img dans la classe product
            image = img['src'] if img   else None #Si image dans la classe, j'affiche la source

            title_tag = product.find('h3').find('a') #Le titre se trouve dans la balise a qui est dans une balise h3
            title = title_tag.get_text() #Affiche le contenu sans les balises


            price_tag = product.find(class_='price_color') #price color correspond a un élément CSS donc je précise sa classe
            price = price_tag.get_text()


            List.append((image,title, price)) #J'ajoute mes éléments trouvé à la liste

print(List) #J'écris la liste

csv_filename = "extracted_links.csv" # Associer le nom du fichier à une variable

with open(csv_filename, "w") as file :
# la fonction permet d'ouvrir un fichier csv pour y écrire des données
# W permet d'écrire dedans

    writer = csv.writer(file) # writer permet d'écrire dans le fichier de manière structuré

    # Écriture des entêtes
    writer.writerow(['Image', 'Title', 'Price'])

    # Écriture des données extraites structuré selon leur catégorie
    writer.writerows(List)

# Commande pour ouvrir le fichier CSV sur l'ordi
os.system(f"open {csv_filename}")
