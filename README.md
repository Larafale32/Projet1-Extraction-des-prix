# Extraction des prix de livres

Ce projet recupere et analyse les informations de livres sur le site "Books to Scrape".

## Structure du projet :
- `source/` : Contient les scripts Python pour le scraping et le traitement des données.
- `data/` : Contient les fichiers CSV generes ou utilises.
- `env/` : Environnement virtuel Python.
- `requirements.txt` : Liste des dependances Python necessaires.

## Instructions :
1. Activer l'environnement virtuel :
   ```
   source env/bin/activate
   ```
2. Installer les dependances :
   ```
   pip install -r requirements.txt
   ```
3. Lancer le script principal :
   ```
   python src/etape1.py
