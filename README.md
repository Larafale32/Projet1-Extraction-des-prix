# **Extraction des Prix de Livres**

Ce projet récupère et analyse les informations des livres disponibles sur le site **Books to Scrape**.

---

## **Introduction**
Ce programme permet une **surveillance automatisée** des prix, catégories et images des livres du site *Books to Scrape*. Les données récupérées peuvent être sauvegardées localement ou exportées dans des fichiers CSV.  

---

## **Structure du Projet**

### **Branche `master`**
- **`main.py`** : Script principal du programme.
- **`requirements.txt`** : Liste des dépendances Python nécessaires.
- **`README.md`** : Description du projet et instructions d'utilisation.
- **`Mail_SAM.docx`** : Explication du programme en tant que pipeline ETL.
- **`.gitignore`** : Définit les fichiers/dossiers à ignorer par Git.

### **Branche secondaire**
- **`source/`** : Contient les étapes intermédiaires et fonctions utilisées pour le scraping.
- **`all_data.zip`** : Données compressées récupérées (incluant des fichiers CSV et des images).

## Instructions :

1. Créer l'environnement 
- `python3 -m env .name_env`

2. Activer l'environnement virtuel :

- `source env/bin/activate`
 
2. Installer les dependances :

- `pip install -r requirements.txt`
  
3. Lancer le script principal :

- `python source/main.py`


## Mode d'Utilisation 

Le programme offre 4 actions, exécutable depuis le terminal : 

### 1- Afficher les informations du livre :

Cette action récupère les infos détaillées d'un seul livre. 

#### commande : 
- `python main.py 1 <URL_du_livre>`

#### exemple :
- `python main.py livre http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html`

### 2- Afficher les informations détaillées de tous les livres d'une catégorie :

Ici, il est important de préciser l'index de la catégorie, qui se caractérise par "_" suivi du nombre qui lui est associé

Toutes les catégories sont inscrites ci-dessous : 

travel_2 / mystery_3 / historical-fiction_4 / sequential-art_5 / classics_6 / philosophy_7 / romance_8 / 
womens-fiction_9 / fiction_10 / childrens_11 / religion_12 / nonfiction_13 / music_14 / default_15 / 
science-fiction_16 / sports-and-games_17 / add-a-comment_18 / fantasy_19 / new-adult_20 / young-adult_21 / science_22 /
poetry_23 / paranormal_24 / art_25 / psychology_26 / autobriography_27 / parenting_28 / adult_fiction_29 / humor_30 /
horror_31 / history_32 / food-and-drink_33 / christian-fiction_34 / business_35 / biography_36 / thriller_37 /
contemporary_38 / spirituality_39 / academic_40 / self_help_41 / historical_42 / christian_43 / suspense_44 /
short-stories_45 / novels_46 / health_47 / politics_48 / cultural_49 / erotica_50 / crime_51. 

#### commande : 
- `python main.py category <categorie_nombre>`

#### exemple : 
- `python3 main.py category fantasy_19`

### 3- Affciher les informations détaillées de tous les livres du site :

#### commande :
- `python3 main.py all books 50`

### 4- Sauvegarder dans un fichier local toutes les images de tous les livres du site : 

#### commande :
- `python3 main.py all images 50`





