

from fonctions import find_book, save_to_csv

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Récupérer les informations du produit
book_data = find_book(url)

# Afficher les données récupérées
print("Données récupérées pour le livre :")
print(book_data)

# Sauvegarder les données dans un fichier CSV
csv_filename = "info_livre.csv"
save_to_csv(csv_filename, book_data)  # Passer book_data comme une liste de liste


# URL de la page du livre dont je souhaite récup les infos
