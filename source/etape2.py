from fonctions import find_books

url = "http://books.toscrape.com/catalogue/category/books/fantasy_19/"

# Appel de la fonction pour récupérer les livres et sauvegarder dans un fichier CSV
find_books(url)
