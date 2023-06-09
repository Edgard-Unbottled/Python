import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook
from tqdm import tqdm
import re

# Liste des URLs à scraper
urls = [

        "https://unbottled.co/products/duo-gommages-visage-corps",
        "https://unbottled.co/products/duo-de-bougies-vegetales-parfumees",
        "https://unbottled.co/products/duo-de-deos-fleuri-cheri-menthe-ole",
        "https://unbottled.co/products/duo-nettoyants-detox-super-doux",       
        "https://unbottled.co/products/duo-de-savons-mains-surgras-et-leurs-porte-savons",
        "https://unbottled.co/products/duo-douceur",
        "https://unbottled.co/products/duo-demaquillant-nettoyant-visage",
        "https://unbottled.co/products/duo-gel-douche-abricot-soin-lavant-intime",
        "https://unbottled.co/products/duo-gel-douche-avoine-soin-lavant-intime",
        "https://unbottled.co/products/duo-de-gels-douche-avoine-abricot",
        "https://unbottled.co/products/duo-gommage-corps-gel-douche-abricot",
        "https://unbottled.co/products/duo-gommage-corps-gel-douche-avoine",
        "https://unbottled.co/products/duo-mini-corps-cheveux-et-la-recy-trousse",
        "https://unbottled.co/products/duo-shampoing-cheveux-colores-apres-shampoing",
        "https://unbottled.co/products/duo-shampoing-cheveux-gras-apres-shampoing",
        "https://unbottled.co/products/duo-shampoing-cheveux-secs-apres-shampoing",
        "https://unbottled.co/products/duo-shampoing-cuir-chevelu-sensible-apres-shampoing",
        "https://unbottled.co/products/duo-shampoing-tout-type-de-cheveux-apres-shampoing",
        "https://unbottled.co/products/pack-famille",
        "https://unbottled.co/products/pack-famille-nombreuse",
        "https://unbottled.co/products/pack-famille-xl",
        "https://unbottled.co/products/pack-gel-douche-abricot-intime-gommage",
        "https://unbottled.co/products/pack-gel-douche-soin-intime-rasage",
        "https://unbottled.co/products/trio-demaquillant-nettoyant-gommage-visage",
        "https://unbottled.co/products/pack-routine-visage-complete",
        "https://unbottled.co/products/gels-douche-x2-soin-lavant-intime",
        "https://unbottled.co/products/trio-de-maxi-gels-douche",
        "https://unbottled.co/products/trio-gels-douche-avoine-abricot-bebe",
        "https://unbottled.co/products/deodorant-fleuri-cheri",

        ]


# Créer un classeur Excel
workbook = Workbook()

# Itérer sur la liste des URLs
for url in tqdm(urls):
    # Faire une requête GET pour récupérer le contenu HTML de la page
    response = requests.get(url)

    # Utiliser BeautifulSoup pour parser le contenu HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Titre de la page
    title = soup.title.string.strip()

    # Nettoyer le titre pour le rendre valide comme titre d'onglet
    title = re.sub(r"[\/:*?<>|]", "-", title)  # Remplace les caractères invalides par "-"

    # Récupérer tous les éléments de question et réponse de la page
    question_elements = soup.select(".faq-list__item-question")
    answer_elements = soup.select(".faq-list__item-answer p")

    # Vérifier si des éléments de question et réponse ont été trouvés
    if question_elements and answer_elements:
        # Créer un nouvel onglet dans le classeur Excel avec le titre de la page
        sheet = workbook.create_sheet(title=title)

        # Écrire les en-têtes dans le nouvel onglet
        sheet.append(["Question", "Réponse"])

        # Itérer sur les éléments de question et réponse et les écrire dans le nouvel onglet
        for question_element, answer_element in zip(question_elements, answer_elements):
            question = question_element.text.strip()
            reponse = answer_element.text.strip()
            sheet.append([question, reponse])

# Supprimer l'onglet par défaut
workbook.remove(workbook["Sheet"])

# Enregistrer le classeur Excel
workbook.save("resultats-faq.xlsx")


    
