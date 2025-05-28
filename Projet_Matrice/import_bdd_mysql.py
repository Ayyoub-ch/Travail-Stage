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
        cursor.execute("""SELECT competence1, categorie, niveau FROM hard
                       JOIN niveau_hard ON niveau 
                       WHERE hard.id=niveau_hard.id_hard 
                       AND niveau_hard.id_personne=(SELECT id FROM personne WHERE id=%s)""", (id_personne,))
        hard_skills = [
            {"competence1": row[0], "categorie": row[1], "niveau": row[2]} for row in cursor.fetchall()
        ]

        # Soft Skills
        cursor.execute("SELECT competence2 FROM soft")
        soft_skills = [
            {"competence2": row[0]} for row in cursor.fetchall()
        ]

        # Niveaux Hard (exemple: id_personne, id_hard, niveau)
        cursor.execute("SELECT id_personne, id_hard , niveau FROM niveau_hard")
        niveaux_hard = [
            {"id_personne": row[0], "id_hard": row[1]} for row in cursor.fetchall()
        ]

        # Niveaux Soft (exemple: id_personne, id_soft, niveau)
        cursor.execute("SELECT id_personne, id_soft, niveau FROM niveau_soft")
        niveaux_soft = [
            {"id_personne": row[0], "id_soft": row[1], "niveau": row[2]} for row in cursor.fetchall()
        ]

        return personnes, hard_skills, soft_skills, niveaux_hard, niveaux_soft

    finally:
        conn.close()
