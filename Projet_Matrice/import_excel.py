import pandas as pd
import mysql.connector

# === Configuration ===
fichier_excel = "Matrice_Nicolas_Morigny.xlsx"
feuille_soft = "Matrice soft skills"
feuille_hard = "Matrice hard skills"

# Connexion à MySQL
def connexion_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )

# Lecture des feuilles Excel
def lire_excel():
    try:
        excel_file = pd.ExcelFile(fichier_excel)

        # Lecture des métadonnées (A1 et A2) sans header
        df_soft_meta = pd.read_excel(excel_file, sheet_name=feuille_soft, header=None)
        df_soft_data = pd.read_excel(excel_file, sheet_name=feuille_soft, skiprows=5)
        df_hard = pd.read_excel(excel_file, sheet_name=feuille_hard)

        #vérifier à partir de l'extraction robuste

        # Extraction des infos personnelles
        nom_prenom_cell = str(df_soft_meta.iloc[1])
        poste_cell = str(df_soft_meta.iloc[2])

        print("Contenu brut A1 :", nom_prenom_cell)
        print("Contenu brut A2 :", poste_cell)

        # Extraction robuste du nom, prénom et poste
        nom_prenom = ""
        poste = ""

        if ":" in nom_prenom_cell:
            nom_prenom = nom_prenom_cell.split(":")[1].strip()
        else:
            nom_prenom = nom_prenom_cell.strip()

        if ":" in poste_cell:
            poste = poste_cell.split(":")[1].strip()
        else:
            poste = poste_cell.strip()

        # Traitement du nom et prénom
        parts = nom_prenom.split()
        if len(parts) >= 2:
            prenom = parts[0]
            nom = " ".join(parts[1:])
        else:
            prenom = nom_prenom
            nom = ""

        df_personnes = pd.DataFrame([{
            "Nom": nom,
            "Prénom": prenom,
            "Poste": poste
        }])

        # Traitement des compétences
        df_soft_data = df_soft_data.rename(columns={df_soft_data.columns[0]: "Compétence"})
        df_soft_data["Type"] = "Soft"
        df_hard["Type"] = "Hard"

        # Fusion
        df_competences = pd.concat([df_hard, df_soft_data], ignore_index=True)

        # Logs
        print("Nom :", nom)
        print("Prénom :", prenom)
        print("Poste :", poste)
        print("Compétences extraites :")
        print(df_competences.head())

        return df_personnes, df_competences

    except Exception as e:
        print("❌ Erreur lors de la lecture Excel :", e)
        return None, None


# Insertion dans la base
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

        # Insertion hard skills
        df_hard = df_competences[df_competences["Type"] == "Hard"]
        for _, row in df_hard.iterrows():
            if "Compétence" in row and "Catégorie" in row:
                cursor.execute(
                    "INSERT INTO hard (competence1, categorie) VALUES (%s, %s)",
                    (row["Compétence"], row["Catégorie"])
                )

        # Insertion soft skills
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

# Exécution principale
if __name__ == "__main__":
    df_personnes, df_competences = lire_excel()

    if df_personnes is not None and df_competences is not None:
        print("\n== Colonnes Personne ==")
        print(df_personnes.columns.tolist())

        print("\n== Colonnes Compétences ==")
        print(df_competences.columns.tolist())

        inserer_donnees(df_personnes, df_competences)
    else:
        print("❌ Aucune donnée insérée.")
