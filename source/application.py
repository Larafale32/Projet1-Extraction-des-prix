
from fonctions import save_to_csv, find_book, find_all_books, find_books, find_all_images

print("Bienvenue sur le sercice de surveillance du site Book to Scrape")

action1 = input("Veuillez sélectionner une action : 1, 2, 3, ou 4.\n 1) Afficher les informations sur un livre\n "
      "2) Afficher les informations de tous les livres d'une catégorie\n 3) Afficher les informations de "
      "tous les libres\n 4) Télécharger toutes les images des livres du site ")

if action1 == "1" :
    print("Veuillez entrer l'URL du livre à afficher.")
    url_livre = input("URL du livre : ")
    book_data = find_book(url_livre)
    print(book_data)
    csv_filename = "info_livre.csv"
    save_to_csv(csv_filename, [book_data])

elif action1 == "2" :
    print("Veuillez entrer le nom de la catégorie pour afficher les informations.")
    category = input("Nom de la catégorie, suivi de _index,\n Exemple : fantasy_19 : ")
    num_pages = int(input("Nombre de pages : "))
    find_books("http://books.toscrape.com/catalogue/category/books/", category, num_pages)

elif action1 == "3":
    num_pages = int(input("Nombre de pages à scraper : "))
    find_all_books(num_pages)

elif action1 == "4":
    num_pages = int(input("Nombre de pages à scraper : "))
    find_all_images(num_pages)
