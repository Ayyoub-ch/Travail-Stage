import pandas as pd


df = pd.read_excel("Matrice_Nicolas_Morigny.xlsx", sheet_name="Matrice Hard Skills")  # Remplace par ton fichier réel

for ligne in df:
    insert_personne(nom)