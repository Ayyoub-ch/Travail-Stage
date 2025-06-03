# import_bdd_mysql.py

import mysql.connector

def get_personn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT nom, prenom, id FROM personne")
    personne = cursor.fetchall()
    conn.close() 
    return personne

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

        cursor.close()

        cursor = conn.cursor()

        # Soft Skills
        cursor.execute("""SELECT soft.competence2, niveau_soft.niveau
                        FROM soft
                        JOIN niveau_soft ON soft.id = niveau_soft.id_soft
                        WHERE niveau_soft.id_personne = %s""", (id_personne,))
        
        soft_skills = [
            {"competence2": row[0], "niveau": row[1]} for row in cursor.fetchall()
        ]
        
        cursor.close()

        
        return personnes, hard_skills, soft_skills

    finally:
        conn.close()

def recherche(id_personne):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )
    cursor1 = conn.cursor()
    cursor1.execute("""
        SELECT 
            personne.id,
            personne.nom, 
            personne.prenom, 
            personne.poste,
            hard.competence1, 
            hard.categorie, 
            niveau_hard.niveau
        FROM hard
        JOIN niveau_hard ON hard.id = niveau_hard.id_hard
        JOIN personne ON niveau_hard.id_personne = personne.id
        WHERE personne.id = %s
    """, (id_personne,))
    hard_results = cursor1.fetchall()
    cursor1.close()

    cursor2 = conn.cursor()
    cursor2.execute("""
        SELECT 
            personne.id,
            personne.nom, 
            personne.prenom, 
            personne.poste, 
            soft.competence2, 
            niveau_soft.niveau
        FROM soft
        JOIN niveau_soft ON soft.id = niveau_soft.id_soft
        JOIN personne ON niveau_soft.id_personne = personne.id
        WHERE personne.id = %s
    """, (id_personne,))
    soft_results = cursor2.fetchall()
    cursor2.close()

    conn.close()
    return hard_results, soft_results


