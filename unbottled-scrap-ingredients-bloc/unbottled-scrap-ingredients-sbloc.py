import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

# Liste des URLs à scraper
urls = [
    "https://unbottled.co/products/shampoing-solide-tout-nu",
    "https://unbottled.co/products/nettoyant-visage-super-doux",
    "https://unbottled.co/products/gel-douche-sans-bouteille",
    "https://unbottled.co/products/trio-bye-bye-plastique",
    "https://unbottled.co/products/maxi-gel-douche-avoine-amande",
    "https://unbottled.co/products/maxi-gel-douche-abricot-karite",
    "https://unbottled.co/products/maxi-savon-neutre-bebes-grands",
    "https://unbottled.co/products/duo-mini-corps-cheveux",
    "https://unbottled.co/products/shampoing-solide-tout-nu-cheveux-gras",
    "https://unbottled.co/products/shampoing-solide-tout-nu-cheveux-secs",
    "https://unbottled.co/products/savon-surgras-mains-toutes-douces",
    "https://unbottled.co/products/savon-surgras-stop-mains-seches",
    "https://unbottled.co/products/gel-douche-sans-bouteille-abricot-karite",
    "https://unbottled.co/products/apres-shampoing-solide-cheveux-soyeux",
    "https://unbottled.co/products/soin-lavant-doux-pour-le-minou",
    "https://unbottled.co/products/gommage-visage-peau-radieuse",
    "https://unbottled.co/products/gommage-corps-peau-neuve",
    "https://unbottled.co/products/soin-de-rasage-au-poil",
    "https://unbottled.co/products/demaquillant-efface-tout",
    "https://unbottled.co/products/bougie-bergamote-romarin",
    "https://unbottled.co/products/bougie-framboise-feve-tonka",
    "https://unbottled.co/products/savon-neutre-bebes-grands",
    "https://unbottled.co/products/nettoyant-masque-detox",
    "https://unbottled.co/products/shampoing-solide-tout-nu-cheveux-colores",
    "https://unbottled.co/products/shampoing-solide-tout-nu-cuir-chevelu-sensible",
    "https://unbottled.co/products/deodorant-fleuri-cheri",
    "https://unbottled.co/products/deodorant-menthe-ole",
    "https://unbottled.co/products/duo-de-bougies-vegetales-parfumees",
    "https://unbottled.co/products/duo-de-deos-fleuri-cheri-menthe-ole",
    "https://unbottled.co/products/duo-de-gels-douche-avoine-abricot",
    "https://unbottled.co/products/duo-demaquillant-nettoyant-visage",
    "https://unbottled.co/products/duo-de-savons-mains-surgras-et-leurs-porte-savons",
    "https://unbottled.co/products/duo-douceur",
    "https://unbottled.co/products/duo-gel-douche-abricot-soin-lavant-intime",
    "https://unbottled.co/products/duo-gel-douche-avoine-soin-lavant-intime",
    "https://unbottled.co/products/duo-gommage-corps-gel-douche-abricot",
    "https://unbottled.co/products/duo-gommage-corps-gel-douche-avoine",
    "https://unbottled.co/products/duo-gommages-visage-corps",
    "https://unbottled.co/products/duo-mini-corps-cheveux-et-la-recy-trousse",
    "https://unbottled.co/products/duo-nettoyants-detox-super-doux",
    "https://unbottled.co/products/duo-shampoing-cheveux-colores-apres-shampoing",
    "https://unbottled.co/products/duo-shampoing-cheveux-gras-apres-shampoing",
    "https://unbottled.co/products/duo-shampoing-cheveux-secs-apres-shampoing",
    "https://unbottled.co/products/duo-shampoing-cuir-chevelu-sensible-apres-shampoing",
    "https://unbottled.co/products/duo-shampoing-tout-type-de-cheveux-apres-shampoing",
    "https://unbottled.co/products/gels-douche-x2-soin-lavant-intime",
    "https://unbottled.co/products/maxi-pack-famille-nombreuse-bebes-grands",
    "https://unbottled.co/products/pack-famille",
    "https://unbottled.co/products/pack-famille-deo",
    "https://unbottled.co/products/pack-famille-nombreuse",
    "https://unbottled.co/products/pack-gel-douche-abricot-intime-gommage",
    "https://unbottled.co/products/pack-gel-douche-soin-intime-rasage",
    "https://unbottled.co/products/pack-routine-visage-complete",
    "https://unbottled.co/products/trio-demaquillant-nettoyant-gommage-visage",
    "https://unbottled.co/products/trio-de-maxi-gels-douche",
    "https://unbottled.co/products/trio-gels-douche-avoine-abricot-bebe",
        ]

# Ouvrir un fichier CSV pour écrire les résultats
with open("resultats-ingredients.csv", "w", encoding='utf-8-sig', newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["URL", 
                     "Titre", 
                     "h3",
                     "Description",
                     "Url Image",
                     ])


    # Itérer sur la liste des URLs
    for url in tqdm(urls):
        # Faire une requête GET pour récupérer le contenu HTML de la page
        response = requests.get(url)

        # Utiliser BeautifulSoup pour parser le contenu HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Titre
        try:
            title = soup.find("h1", {"class": ["product-title"]}).text
        except AttributeError:
            title = "N/A"

        # h3
        try:
            h3 = soup.find("h3", {"class": ["my_eco_heading"]}).text
        except AttributeError:
            h3 = "N/A"

        # Description
        try:
            description = soup.find("div", {"class": ["my_eco_small_text"]}).text
        except AttributeError:
            description = "N/A"

        # Url Image
        try:
            image_url = soup.find("div", {"class": ["zoom_ingredient_image"]}).find("img")["src"] 
        except (AttributeError, KeyError):
            image_url = "N/A"

        # Écrire les résultats dans le fichier CSV
        writer.writerow([url, title, h3, description, image_url])


    
