# import_bdd_mysql.py

import mysql.connector

def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )

    try:
        cursor = conn.cursor()

        # Personnes
        cursor.execute("SELECT nom, prenom, poste FROM personne")
        personnes = cursor.fetchall()

        # Hard Skills
        cursor.execute("SELECT competence1, categorie FROM hard")
        hard_skills = [
            {"competence1": row[0], "categorie": row[1]} for row in cursor.fetchall()
        ]

        # Soft Skills
        cursor.execute("SELECT competence2 FROM soft")
        soft_skills = [
            {"competence2": row[0]} for row in cursor.fetchall()
        ]

        return personnes, hard_skills, soft_skills

    finally:
        conn.close()
