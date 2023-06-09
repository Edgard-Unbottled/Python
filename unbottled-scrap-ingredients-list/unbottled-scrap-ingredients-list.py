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
        "https://unbottled.co/products/deodorant-fleuri-cheri",
        "https://unbottled.co/products/deodorant-menthe-ole",

        ]

# Ouvrir un fichier CSV pour écrire les résultats
with open("list-ingredients.csv", "w", encoding='utf-8', newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["URL", 
                     "Titre", 
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

        # Liste Ingrédients
        list_ing = soup.find_all("li", {"class": "my_shampoo_INCI_ingredient"})  # Recherche tous les éléments avec la classe "my_shampoo_INCI_ingredient"
        list_ing_result = []  # Initialisation de la liste des résultats
        # print(len(list_ing))
        for element in list_ing:
            # Pour chaque élément avec la classe "my_shampoo_INCI_ingredient", recherche les éléments avec les classes "titre", "images" et "description"
            tabindex = element.find("span", {"tabindex": "0"}).text.strip() if element.find("span", {"tabindex": "0"}) else 'none'

            list_ing_result.append([tabindex])
            

        # Écrire les résultats dans le fichier CSV
        writer.writerow([url, title, "#".join("@".join(map(str, ingredient)) for ingredient in list_ing_result)])


    
