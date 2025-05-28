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
        cursor.execute("SELECT nom, prenom, poste, id FROM personne")
        personnes = cursor.fetchall()
        id_personne=personnes[0][3]

        # Hard Skills
        cursor.execute("""SELECT hard.competence1, hard.categorie, niveau_hard.niveau
                        FROM hard
                        JOIN niveau_hard ON hard.id = niveau_hard.id_hard
                        WHERE niveau_hard.id_personne = %s""", (id_personne,))
        hard_skills = [
            {"competence1": row[0], "categorie": row[1], "niveau": row[2]} for row in cursor.fetchall()
        ]

        # Soft Skills
        cursor.execute("""SELECT soft.competence2, niveau_soft.niveau
                        FROM soft
                        JOIN niveau_soft ON soft.id = niveau_soft.id_soft
                        WHERE niveau_soft.id_personne = (SELECT id FROM personne WHERE id = %s)""", (id_personne,))
        soft_skills = [
            {"competence2": row[0], "niveau": row[1]} for row in cursor.fetchall()
        ]

        
        return personnes, hard_skills, soft_skills

    finally:
        conn.close()
