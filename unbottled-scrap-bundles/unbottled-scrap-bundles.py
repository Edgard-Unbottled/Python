import glob
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

# Chemin du dossier contenant les fichiers HTML
folder_path = "C:/Users/edgar/Documents/dev/sandbox/bundles"

# Liste des fichiers HTML à scraper
file_paths = glob.glob(folder_path + "/*.html")

# Fonction pour extraire le texte brut d'une balise en prenant en compte les balises enfants
def extract_text(tag):
    if tag is None:
        return ''
    else:
        return ''.join(tag.get_text(strip=True, separator=' ') for tag in tag.find_all(recursive=False))

# Ouvrir un fichier CSV pour écrire les résultats
with open("resultats-bundles.csv", "w", encoding='utf-8', newline="") as f:
    writer = csv.writer(f, delimiter=";")

    # Itérer sur la liste des fichiers HTML
    for file_path in tqdm(file_paths):
        # Lire le contenu HTML du fichier
        with open(file_path, "r", encoding='utf-8') as html_file:
            html_content = html_file.read()

        # Utiliser BeautifulSoup pour parser le contenu HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Récupérer toutes les balises <p> et les balises <pre>
        p_tags = soup.find_all("p")
        pre_tags = soup.find_all("pre")

        # Récupérer les textes des balises <p> et les balises <pre>
        p_texts = [extract_text(tag) for tag in p_tags]
        pre_texts = [extract_text(tag) for tag in pre_tags]

        # Écrire les résultats dans le fichier CSV pour le fichier HTML actuel
        row = [file_path] + p_texts + pre_texts
        writer.writerow(row)
