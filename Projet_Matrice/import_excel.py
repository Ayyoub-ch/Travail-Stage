import pandas as pd
import mysql.connector
import re

# === Configuration ===
fichier_excel = "Matrice_Nicolas_Morigny.xlsx"
feuille_soft = "Matrice soft skills"
feuille_hard = "Matrice hard skills"

# === Connexion à la base de données ===
def connexion_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )

# === Lecture et traitement du fichier Excel ===
def lire_excel():
    try:
        excel_file = pd.ExcelFile(fichier_excel)

        # Métadonnées (nom, prénom, poste) depuis feuille soft
        df_soft_meta = pd.read_excel(excel_file, sheet_name=feuille_soft, header=None)
        nom_prenom_cell = df_soft_meta.iloc[1, 0]
        poste_cell = df_soft_meta.iloc[2, 0]
        """ au final il fallait UNIQUEMENT CHANGER LES NUMEROS PAR RAPPORT AUX LIGNES DU EXCEL, parfois réfléchir tranquillement c'est bien"""

        print("🔍 A1 :", repr(nom_prenom_cell))
        print("🔍 A2 :", repr(poste_cell))

        # Nettoyage des métadonnées

        if ":" in nom_prenom_cell:
            nom_prenom = nom_prenom_cell.split(":", 1)[1].strip()
        else:
            nom_prenom = nom_prenom_cell.strip()

        if ":" in poste_cell:
            poste = poste_cell.split(":", 1)[1].strip()
        else:
            poste = poste_cell.strip()

        # Suppression des parasites
        nom_prenom = re.sub(r"\b(?:\d+|Na|nan|None)\b", "", nom_prenom).strip()
        poste = re.sub(r"\b(?:\d+|Na|nan|None)\b", "", poste).strip()

        # Découpe prénom / nom
        parts = nom_prenom.split()
        prenom = parts[0] if parts else ""
        nom = " ".join(parts[1:]) if len(parts) > 1 else ""

        print("✅ Prénom :", prenom)
        print("✅ Nom :", nom)
        print("✅ Poste :", poste)

        df_personnes = pd.DataFrame([{
            "Nom": nom,
            "Prénom": prenom,
            "Poste": poste
        }])

        # Lecture des compétences
        df_soft_data = pd.read_excel(excel_file, sheet_name=feuille_soft, skiprows=6)
        df_hard = pd.read_excel(excel_file, sheet_name=feuille_hard, skiprows=6)

        print(df_soft_data)

    except Exception as e:
        print("❌ Erreur lors de la lecture du fichier Excel :", e)
        return None, None

# === Insertion dans la base ===
def inserer_donnees(df_personnes, df_competences):
    if df_personnes is None or df_competences is None:
        print("❌ Données non valides.")
        return

    conn = connexion_mysql()
    cursor = conn.cursor()

    try:
        # Suppression des anciennes données
        cursor.execute("DELETE FROM personne")
        cursor.execute("DELETE FROM hard")
        cursor.execute("DELETE FROM soft")

        # Insertion personne
        for _, row in df_personnes.iterrows():
            cursor.execute(
                "INSERT INTO personne (nom, prenom, poste) VALUES (%s, %s, %s)",
                (row["Nom"], row["Prénom"], row["Poste"])
            )

        # Insertion des compétences
        df_hard = df_competences[df_competences["Type"] == "Hard"]
        for _, row in df_hard.iterrows():
            if "Compétence" in row and "Catégorie" in row:
                cursor.execute(
                    "INSERT INTO hard (competence1, categorie) VALUES (%s, %s)",
                    (row["Compétence"], row["Catégorie"])
                )

        df_soft = df_competences[df_competences["Type"] == "Soft"]
        for _, row in df_soft.iterrows():
            if "Compétence" in row:
                cursor.execute(
                    "INSERT INTO soft (competence2) VALUES (%s)",
                    (row["Compétence"],)
                )

        conn.commit()
        print("✅ Données insérées avec succès.")

    except Exception as e:
        conn.rollback()
        print("❌ Erreur lors de l'insertion :", e)

    finally:
        conn.close()

# === Exécution principale ===
if __name__ == "__main__":
    df_personnes, df_competences = lire_excel()

    if df_personnes is not None and df_competences is not None:
        print("\n📋 Colonnes Personne :", df_personnes.columns.tolist())
        print("📋 Colonnes Compétences :", df_competences.columns.tolist())
        inserer_donnees(df_personnes, df_competences)
    else:
        print("❌ Aucune donnée insérée.")
