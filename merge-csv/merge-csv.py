import pandas as pd
import os
from tqdm import tqdm

def aggregate_csv_files(input_dir, output_filename):
    """
    Cette fonction agrège plusieurs fichiers CSV en un seul fichier.

    Args:
    - input_dir (str) : Le dossier contenant les fichiers CSV à agréger.
    - output_filename (str) : Le chemin du fichier de sortie.

    Returns:
    None
    """

    # Récupération de la liste des fichiers CSV dans le dossier spécifié
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    # Trier la liste des fichiers CSV par ordre croissant (en se basant sur le numéro à la fin du nom du fichier)
    csv_files = sorted(csv_files, key=lambda x: int(x.split('_')[-1].split('.csv')[0]))

    # Information sur le nombre de fichiers trouvés
    print(f"Found {len(csv_files)} CSV files.")

    # Lecture du premier fichier pour initialiser les données agrégées
    aggregated_data = pd.read_csv(os.path.join(input_dir, csv_files[0]), dtype=str)

    # Utilisation de tqdm pour afficher une barre de progression lors de la lecture et de l'agrégation des fichiers CSV
    for csv_file in tqdm(csv_files[1:], desc="Processing CSV files"):
        # Lecture du fichier CSV actuel
        data = pd.read_csv(os.path.join(input_dir, csv_file), header=0, dtype=str)
        # Agrégation du fichier CSV actuel avec les données précédentes
        aggregated_data = pd.concat([aggregated_data, data], ignore_index=True)

    # Écriture des données agrégées dans le fichier de sortie
    print(f"Writing data to {output_filename}...")
    aggregated_data.to_csv(output_filename, index=False)
    print("Done!")

# Exemple d'utilisation
if __name__ == "__main__":
    input_directory = "C:\\Users\\EdgardTroadec\\Documents\\python\\merge-csv\\sources"
    output_file = "C:\\Users\\EdgardTroadec\\Documents\\python-data\\merge-csv\\fichier_agregé.csv"
    aggregate_csv_files(input_directory, output_file)
