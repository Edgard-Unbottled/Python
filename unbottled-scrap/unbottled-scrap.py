import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

# Liste des URLs à scraper
urls = [

        "https://unbottled.co/products/shampoing-solide-tout-nu",
        "https://unbottled.co/products/nettoyant-visage-super-doux",
        "https://unbottled.co/products/gel-douche-sans-bouteille",
        "https://unbottled.co/products/maxi-gel-douche-avoine-amande",       
        "https://unbottled.co/products/shampoing-solide-tout-nu-cheveux-gras",
        "https://unbottled.co/products/shampoing-solide-tout-nu-cheveux-secs",
        "https://unbottled.co/products/savon-surgras-mains-toutes-douces",
        "https://unbottled.co/products/savon-surgras-stop-mains-seches",
        "https://unbottled.co/products/gel-douche-sans-bouteille-abricot-karite",
        "https://unbottled.co/products/maxi-gel-douche-abricot-karite",
        "https://unbottled.co/products/apres-shampoing-solide-cheveux-soyeux",
        "https://unbottled.co/products/soin-lavant-doux-pour-le-minou",
        "https://unbottled.co/products/gommage-visage-peau-radieuse",
        "https://unbottled.co/products/gommage-corps-peau-neuve",
        "https://unbottled.co/products/soin-de-rasage-au-poil",
        "https://unbottled.co/products/demaquillant-efface-tout",
        "https://unbottled.co/products/savon-neutre-bebes-grands",
        "https://unbottled.co/products/maxi-savon-neutre-bebes-grands",
        "https://unbottled.co/products/nettoyant-masque-detox",
        "https://unbottled.co/products/shampoing-solide-tout-nu-cheveux-colores",
        "https://unbottled.co/products/shampoing-solide-tout-nu-cuir-chevelu-sensible",

        ]

# Ouvrir un fichier CSV pour écrire les résultats
with open("resultats.csv", "w", encoding='utf-8', newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["URL", 
                     "Titre", 
                     "Sous Titre 1", 
                     "Sous Titre 2", 
                     "Description 1", 
                     "Description 2", 
                     "Description 3", 
                     "Economie",
                     "Tabs",
                     "Promesse Titre",
                     "Promesse Description",
                     "Super IngrédientsTitre",
                     "Super Ingrédients Description",
                     "Liste Ingrédients",
                     ])


    # Itérer sur la liste des URLs
    for url in tqdm(urls):
        # Faire une requête GET pour récupérer le contenu HTML de la page
        response = requests.get(url)

        # Utiliser BeautifulSoup pour parser le contenu HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Titre
        title = soup.find("h1", {"class": ["product-title"]}).text

        # Sous Titre 1
        subtitle1 = soup.find("h3", {"class": ["product-subtitle-v1"]}).text  

        # Sous Titre 2
        subtitle2 = soup.find("h2", {"class": ["product-subtitle-v2"]}).prettify().replace("\n", "")

        # Description 1
        desc1 = soup.find("div", {"class": "my_product_description_v2"}).find("span").prettify().replace("\n", "")

        # Description 2
        desc2 = soup.find("div", {"class": "my_product_description_v3"}).find("span").prettify().replace("\n", "")

        # Description 3
        desc3 = soup.find("div", {"class": "my_product_description_v4"}).prettify().replace("\n", "")

        # Economie
        economie = soup.find("div", {"class": "product-g_mobile"}).text

        # Tabs
        tabs = soup.find("div", {"class": "product-tabs"}).prettify().replace("\n", "")

        # Liste Ingrédients
        list_ing = soup.find_all("div", {"class": "my_ingredients_content"})  # Recherche tous les éléments avec la classe "my_ingredients_content"
        list_ing_result = []  # Initialisation de la liste des résultats
        # print(len(list_ing))
        for element in list_ing:
            # Pour chaque élément avec la classe "my_ingredients_content", recherche les éléments avec les classes "emoji", "description" et "p"
            try :
                ingredients_emoji = element.find("div", {"class": "my_ingredients_emoji"}).find("i").get("aria-label") if element.find("div", {"class": "my_ingredients_emoji"}).find("i").get("aria-label") else 'none'
                if ingredients_emoji is None:
                    ingredients_emoji = "unknown"
            except AttributeError:
                print(f"Warning: ingredients_emoji not found for URL {url}")
                continue
            try :
                ingredients_description_p = element.find("div", {"class": "my_ingredients_description"}).find("p").text.strip() if element.find("div", {"class": "my_ingredients_description"}).find("p") else 'none'
            except AttributeError:
                print(f"Warning: ingredients_description p not found for URL {url}")
                continue
            try :
               ingredients_description = element.find("div", {"class": "my_ingredients_description"}).text.strip() if element.find("div", {"class": "my_ingredients_description"}) else 'none'
            except AttributeError:
                print(f"Warning: ingredients_description not found for URL {url}")
                continue
            list_ing_result.append([ingredients_emoji,  ingredients_description_p, ingredients_description])

        # Promesse titre
        prom_title = soup.find("h1", {"class": ["shampoo-title__text-v1"]}).text        

        # Promesse description
        prom_desc = soup.find("div", {"class": ["shampoo-subtitle__text-v1"]}).text 

        # Super Ingrédients titre
        suping_title = soup.find("h3", {"class": ["my_eco_heading"]}).text        

        # Super Ingrédients description
        suping_desc = soup.find("div", {"class": ["my_eco_wrapper"]}).text 
            

        # Écrire les résultats dans le fichier CSV
        #writer.writerow([url, title, subtitle1, subtitle2, desc1, desc2, desc3, economie, tabs, prom_title, prom_desc])
        writer.writerow([url, title, subtitle1, subtitle2, desc1, desc2, desc3, economie, tabs, prom_title, prom_desc, suping_title, suping_desc, ing_detail, "#".join("@".join(map(str, ingredient)) for ingredient in list_ing_result)])


    
