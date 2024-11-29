from fonctions import find_books


category = "fantasy_19"
base_url = "http://books.toscrape.com/catalogue/category/books/"

# Appel de la fonction pour récupérer les livres et sauvegarder dans un fichier CSV
find_books(base_url, category)

#http://books.toscrape.com/catalogue/unicorn-tracks_951/index.html
#http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html