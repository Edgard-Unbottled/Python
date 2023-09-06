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


def index_orders_by_email(orders):
    indexed_orders = {}
    for order in orders:
        order_id, order_email, total_price = order
        if order_email not in indexed_orders:
            indexed_orders[order_email] = []
        indexed_orders[order_email].append((order_id, total_price))
    return indexed_orders

def process_data(emails, indexed_orders):
    data = {}
    emails_set = set(emails)  # Convertir la liste d'emails en ensemble pour une recherche rapide
    for email in tqdm(emails_set, desc="Traitement des emails"):
        if email in indexed_orders:  # Vérifiez si l'email a des commandes associées
            for order in indexed_orders[email]:
                order_id, total_price = order
                total_price_value = float(total_price)
                if email in data:
                    data[email]['total'] += total_price_value
                    data[email]['count'] += 1
                else:
                    data[email] = {'total': total_price_value, 'count': 1}
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

# Indexer les commandes par email
print("Indexation des commandes par email...")
indexed_orders = index_orders_by_email(orders)

# Traiter et agréger les données
aggregated_data = process_data(emails, indexed_orders)

# Écrire les données agrégées dans le fichier final
print("Écriture des données agrégées dans wheelio_orders_agregated.csv...")
write_processed_data_to_csv(aggregated_data, 'C:\\Users\\EdgardTroadec\\Documents\\python\\wheelio-report\\wheelio_orders_agregated.csv')
print("Terminé!")