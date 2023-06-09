import requests
import xml.etree.ElementTree as ET
import csv

# Téléchargement du fichier XML depuis l'URL
response = requests.get('https://unbottled.co/sitemap.xml')
xml_data = response.content
# print(xml_data)

# Analyse du fichier XML et extraction des éléments "loc"
root = ET.fromstring(xml_data)
locs = root.findall('loc')
print(len(locs))

# Ecriture des données dans un fichier CSV
with open('resultats-xml.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for loc in locs:
        writer.writerow([loc.text])