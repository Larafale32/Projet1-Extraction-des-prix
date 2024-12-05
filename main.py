# -*- coding: utf-8 -*-

from fonctions import save_to_csv, find_book, find_all_books, find_books, find_all_images
import sys # module utilisé pour gérer les arguments passé dans le terminal.

#Affiche les instructions pour utiliser le programme.
def instructions():
    print(
        "\nBienvenue sur le service de surveillance du site 'Books to Scrape'.\n"
        "Voici les commandes que vous pouvez exécuter :\n"
        "  1 <URL du livre>          : Afficher les informations sur un livre.\n"
        "  2 <Nom de la catégorie> : Afficher les informations de tous les livres d'une catégorie.\n"
        "  3 <Nombre de pages>       : Afficher les informations de tous les livres.\n"
        "  4 <Nombre de pages>       : Télécharger toutes les images des livres du site.\n"
        "\nExemples :\n"
        "  python3 main.py livre http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html\n"
        "  python3 main.py category fantasy_19 \n"
        "  python3 main.py all books 50\n"
        "  python3 main.py all images 50\n"
    )

# fonction principale qui exécute les actions en fonctions des arguments donnés dans le terminal
def main():
        print("Début du programme")

        # vérification que le nombre d'argument est suffisant
        if len(sys.argv) < 2:  # On vérifie s'il y a assez d'arguments (au moins 1 argument après le nom du script)
            print("Arguments manquants. Voici comment utiliser le programme :")
            instructions()  # Affiche les instructions (s'il n'y a pas assez d'arguments)
            return
        # Création de la variable action
        action = sys.argv[1] # représente le premier argument passé après le nom du script
        print("Action :", action)

        # Vérification que l'actiuon figure bien dans les propositions'
        if action not in ["livre", "category", "all books", "all images"]:
            print("Action non reconnue.")
            instructions()
            return

        if action == "1" and len(sys.argv) < 3: # Vérifie si l'URL est manquante pour l'action 1
            print("URL manquante pour l'action 1.")
            return

        # crétion de la variable param pour y stocker l'URL
        param = sys.argv[2] # L'URL est le deuxieme argements passé dans le terminal
        print("Action :", action, ", Paramètre :", param)

        # Appel des fonctions en fonction de l'action'
        if action == "livre":
            print("Exécution de l'action 1")
            url_livre = param
            book_data = find_book(url_livre)
            print("Données du livre :", book_data)
            csv_filename = "info_livre.csv"
            save_to_csv(csv_filename, book_data)

        elif action == "category":
            print("Exécution de l'action 2")
            category = param
            print("Catégorie :", category)
            find_books("http://books.toscrape.com/catalogue/category/books/", category)

        elif action == "all books":
            print("Exécution de l'action 3")
            find_all_books()

        elif action == "all images":
            print("Exécution de l'action 4")
            num_pages = int(param)
            find_all_images(num_pages)


# Affiche les instructions en cas d'action invalide


if __name__ == "__main__":
    main() # Exécute la fonction principal
