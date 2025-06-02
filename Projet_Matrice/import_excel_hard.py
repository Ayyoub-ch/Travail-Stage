import pandas as pd
import mysql.connector
import re
import hard_skills

# === Configuration ===
fichier_excel = "Matrice_Nicolas_Morigny.xlsx"
feuille_hard = "Matrice hard skills"

# === Connexion MySQL ===
def connexion_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )

# === Lecture du fichier Excel ===
def lire_excel():
    try:
        excel_file = pd.ExcelFile(fichier_excel)

        df_hard_meta = pd.read_excel(excel_file, sheet_name=feuille_hard, header=None)
        nom_prenom_cell = df_hard_meta.iloc[1, 0]
        poste_cell = df_hard_meta.iloc[2, 0]

        nom_prenom = nom_prenom_cell.split(":", 1)[1].strip() if ":" in nom_prenom_cell else nom_prenom_cell.strip()
        poste = poste_cell.split(":", 1)[1].strip() if ":" in poste_cell else poste_cell.strip()

        nom_prenom = re.sub(r"\b(?:\d+|Na|nan|None)\b", "", nom_prenom).strip()
        poste = re.sub(r"\b(?:\d+|Na|nan|None)\b", "", poste).strip()

        parts = nom_prenom.split()
        prenom = parts[0] if parts else ""
        nom = " ".join(parts[1:]) if len(parts) > 1 else ""

        df_personnes = pd.DataFrame([{"Nom": nom, "Prénom": prenom, "Poste": poste}])

        df_hard_data = pd.read_excel(excel_file, sheet_name=feuille_hard, skiprows=5, header=0)

        df_hard_clean = df_hard_data.dropna(how='all')

        df_hard_level = pd.read_excel(excel_file, sheet_name=feuille_hard, skiprows=5, usecols=[2])

        return df_personnes, df_hard_clean, df_hard_level

    except Exception as e:
        print("❌ Erreur lors de la lecture du fichier Excel :", e)
        return None, None, None, None, None


# === Insertion des données ===
def inserer_donnees(df_personnes, df_hard_clean, df_hard_level):
    if any(x is None for x in (df_personnes, df_hard_clean, df_hard_level)):
        print("❌ Données non valides.")
        return

    conn = connexion_mysql()
    cursor = conn.cursor()

    try:
        # Nettoyage
        cursor.execute("DELETE FROM personne")
        cursor.execute("DELETE FROM hard")
        cursor.execute("DELETE FROM niveau_hard")

        # Insertion personne
        for _, row in df_personnes.iterrows():
            cursor.execute(
                "INSERT INTO personne (nom, prenom, poste) VALUES (%s, %s, %s)",
                (row["Nom"], row["Prénom"], row["Poste"])
            )
        cursor.execute("SELECT id FROM personne WHERE nom = %s AND prenom = %s", (row["Nom"], row["Prénom"]))
        id_personne = cursor.fetchone()[0]
        print(f"🧍 ID Personne: {id_personne}")

        # Appel des classes
        hard_inserter = hard_skills.HardSkillInserter(cursor, conn, df_hard_clean, id_personne)
        hard_inserter.inserer()

        print("✅ Données insérées avec succès.")

    except Exception as e:
        print("❌ Erreur lors de l'insertion :", e)
        conn.rollback()

    finally:
        conn.close()

# À la fin de import_excel_hard.py

def run_hard(id_personne):
    df_personnes, df_hard_clean, df_hard_level = lire_excel()
    if df_hard_clean is None:
        print("❌ Données hard invalides.")
        return

    conn = connexion_mysql()
    cursor = conn.cursor()
    try:
        hard_inserter = hard_skills.HardSkillInserter(cursor, conn, df_hard_clean, id_personne)
        hard_inserter.inserer()
        conn.commit()
    except Exception as e:
        print("❌ Erreur lors de l'insertion hard:", e)
        conn.rollback()
    finally:
        conn.close()




# === Exécution principale ===
if __name__ == "__main__":
    result = lire_excel()

    if result and not any(r is None for r in result):
        df_personnes, df_hard_clean, df_hard_level = result

        inserer_donnees(df_personnes, df_hard_clean, df_hard_level)
    else:
        print("❌ Aucune donnée insérée.")
