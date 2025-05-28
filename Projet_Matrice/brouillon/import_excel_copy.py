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

        # Suppression des caractères parasites
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
        df_soft_data = pd.read_excel(excel_file, sheet_name=feuille_soft, skiprows=5, header=0)
        df_hard_data = pd.read_excel(excel_file, sheet_name=feuille_hard, skiprows=5, header=0)

        #si on change 5 par 6 la colonne hard skill sera vide car dans insertion_donnees on vérifie les titres de colonnes du Excel voir plus bas

        # Supprimer les lignes contenant des NaN dans les deux DataFrames
        df_soft_data_clean = df_soft_data.dropna(how='all')  # Supprime les lignes où toutes les valeurs sont NaN
        df_hard_clean = df_hard_data.dropna(how='all')


        # Lecture des niveaux
        df_soft_level = pd.read_excel(excel_file, sheet_name=feuille_soft, skiprows=5, usecols=[1])
        df_hard_level = pd.read_excel(excel_file, sheet_name=feuille_hard, skiprows=5, usecols=[2])

        return df_personnes, df_soft_data_clean, df_hard_clean, df_soft_level, df_hard_level

    

    except Exception as e:
        print("❌ Erreur lors de la lecture du fichier Excel :", e)
        return None, None, None, None, None

# === Insertion dans la base ===
def inserer_donnees(df_personnes, df_soft_data_clean, df_hard_clean, df_soft_level, df_hard_level):
    if any(x is None for x in (df_personnes, df_soft_data_clean, df_hard_clean, df_soft_level, df_hard_level)):
        print("❌ Données non valides.")
        return

    conn = connexion_mysql()
    cursor = conn.cursor()

    try:
        # Suppression des anciennes données
        cursor.execute("DELETE FROM personne")
        cursor.execute("DELETE FROM hard")
        cursor.execute("DELETE FROM soft")
        cursor.execute("DELETE FROM niveau_hard")
        cursor.execute("DELETE FROM niveau_soft")

        # Insertion personne
        for _, row in df_personnes.iterrows():
            cursor.execute(
                "INSERT INTO personne (nom, prenom, poste) VALUES (%s, %s, %s)",
                (row["Nom"], row["Prénom"], row["Poste"])
            )
        cursor.execute("SELECT id FROM personne WHERE nom = %s AND prenom = %s", (row["Nom"], row["Prénom"]))
        IdPrenom = cursor.fetchone()[0]
        print(IdPrenom)

        # Insertion des compétences
    
        
        # Insertion des compétences hard
        for _, row in df_hard_clean.iterrows():
            cursor.execute(
                "INSERT INTO hard (competence1, categorie) VALUES (%s, %s)",
                (row["Hard Skills / outils"], row["Catégorie"])
            )
            cursor.execute("select id from hard WHERE competence1= %s", (row["Hard Skills / outils"],))
            Id_Hard = cursor.fetchone()[0]
            print(Id_Hard)

            if row["Niveau"]> 0:
                cursor.execute(
                "INSERT INTO niveau_hard (id_personne, id_hard, niveau) VALUES (%s, %s, %s)",
                (IdPrenom, Id_Hard, row["Niveau"])
                )
        conn.commit() 
        
        cursor.fetchall()
        
        # Insertion des compétences soft
        for _, row in df_soft_data_clean.iterrows():
            # Insertion de la soft skill dans la table `soft`
            cursor.execute(
                "INSERT INTO soft (competence2) VALUES (%s)",
                (row["Soft Skills"],)
            )
            
            # Récupération de l'ID de la soft skill insérée
            cursor.execute("SELECT id FROM soft WHERE competence2 = %s", (row["Soft Skills"],))
            id_soft = cursor.fetchone()[0]
            print(id_soft)

            
            # Insertion dans `niveau_soft` si le niveau est supérieur à 0
            cursor.execute(
                "INSERT INTO niveau_soft (id_personne, id_soft, niveau) VALUES (%s, %s, %s)",
                (IdPrenom, id_soft, row["."])
            )
        conn.commit() 
            

                
    



        conn.commit()
        print("✅ Données insérées avec succès.")

    except Exception as e:
        #conn.rollback()
        print("❌ Erreur lors de l'insertion :", e)

    finally:
        conn.close()


# === Exécution principale ===
if __name__ == "__main__":
    result = lire_excel()

    if result is not None and len(result) == 5 and not any(r is None for r in result):
        df_personnes, df_soft_data_clean, df_hard_clean, df_soft_level, df_hard_level = result

        print("\n📋 Colonnes Personne :", df_personnes.columns.tolist())
        print("📋 Colonnes Soft :", df_soft_data_clean.columns.tolist())
        print("📋 Colonnes Hard :", df_hard_clean.columns.tolist())
        print(df_hard_clean.head())
        print("📋 Niveaux Soft :", df_soft_level.columns.tolist())
        print("📋 Niveaux Hard :", df_hard_level.columns.tolist())

        inserer_donnees(df_personnes, df_soft_data_clean, df_hard_clean, df_soft_level, df_hard_level)
    else:
        print("❌ Aucune donnée insérée.")

