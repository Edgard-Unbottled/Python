import csv
import os
from tqdm import tqdm


def load_emails_from_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader if row]

def load_orders_from_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Utilisez DictReader pour lire le fichier CSV en tant que dictionnaire
        orders = []
        for row in reader:
            order_id = row['Name']
            order_email = row['Email']
            total_price = row['Total']
            if total_price:  # Ajoutez cette condition pour ignorer les lignes avec "Total" vide
                orders.append((order_id, order_email, total_price))
        return orders


def process_data(emails, orders):
    data = {}
    for email in tqdm(emails, desc="Traitement des emails"):
        for order in orders:
            order_id, order_email, total_price = order
            if email == order_email:
                if email in data:
                    data[email]['total'] += float(total_price)
                    data[email]['count'] += 1
                else:
                    data[email] = {'total': float(total_price), 'count': 1}
    return data

def write_processed_data_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Écrire l'en-tête du CSV
        headers = ["Email", "Total combiné", "Nombre de commandes"]
        writer.writerow(headers)
        
        # Écrire les données
        for email, values in data.items():
            writer.writerow([email, values['total'], values['count']])

# Charger les emails et les commandes
print("Chargement des emails depuis wheelio.csv...")
emails = load_emails_from_csv('C:\\Users\\EdgardTroadec\\Documents\\python\\wheelio-report\\wheelio.csv')
print(f"{len(emails)} emails chargés.")
print("Chargement des commandes depuis all_orders.csv...")
orders = load_orders_from_csv('C:\\Users\\EdgardTroadec\\Documents\\python-data\\wheelio-report\\all_orders.csv')
print(f"{len(orders)} commandes chargées.")

# Traiter et agréger les données
aggregated_data = process_data(emails, orders)

# Écrire les données agrégées dans le fichier final
print("Écriture des données agrégées dans wheelio_orders_agregated.csv...")
write_processed_data_to_csv(aggregated_data, 'wheelio_orders_agregated.csv')
print("Terminé!")

