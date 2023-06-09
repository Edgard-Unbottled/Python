import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook
from tqdm import tqdm
import re

# Liste des URLs à scraper
urls = [
        "https://unbottled.co/products/deodorant-fleuri-cheri",
        "https://unbottled.co/products/deodorant-menthe-ole",

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
    answer_elements = soup.select(".faq-list__item-answer")

    # Vérifier si des éléments de question et réponse ont été trouvés
    if question_elements and answer_elements:
        # Créer un nouvel onglet dans le classeur Excel avec le titre de la page
        sheet = workbook.create_sheet(title=title)

        # Écrire les en-têtes dans le nouvel onglet
        sheet.append(["Question", "Réponse"])

        # Itérer sur les éléments de question et réponse et les écrire dans le nouvel onglet
        for question_element, answer_element in zip(question_elements, answer_elements):
            question = question_element.text.strip()

            # Concaténer tous les éléments <p> en une seule chaîne de texte
            answer = ' '.join([p.text.strip() for p in answer_element.select("p")])

            sheet.append([question, answer])

# Supprimer l'onglet par défaut
workbook.remove(workbook["Sheet"])

# Enregistrer le classeur Excel
workbook.save("resultats-faq-single.xlsx")


    
