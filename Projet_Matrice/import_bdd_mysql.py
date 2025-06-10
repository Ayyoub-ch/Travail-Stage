# import_bdd_mysql.py

import mysql.connector


def get_all_hard_competences():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT id, competence1 FROM hard ORDER BY competence1")
        result = cursor.fetchall()
        cursor.close()
        return result  # Liste de tuples : [(1, "Python"), (2, "SQL"), ...]
    finally:
        conn.close()




def get_personn(intercontrat=0):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )
    cursor = conn.cursor()

    if intercontrat:
        cursor.execute("SELECT id, nom, prenom FROM personne WHERE intercontrat = 1")
    else:
        cursor.execute("SELECT id, nom, prenom FROM personne")

    personnes = cursor.fetchall()
    cursor.close()
    conn.close()
    return personnes



def get_comp(id_hard):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )

    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute("""SELECT hard.competence1, hard.categorie, niveau_hard.niveau
                        FROM hard
                        JOIN niveau_hard ON hard.id = niveau_hard.id_hard
                        WHERE niveau_hard.id_hard = %s""", (id_hard,))
        hard_skills = [
            {"competence1": row[0], "categorie": row[1], "niveau": row[2]} for row in cursor.fetchall()
        ]
        cursor.close()
        return hard_skills
    
    finally:
        conn.close()


def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )

    try:
        cursor = conn.cursor(buffered=True)

        # Personnes
        cursor.execute("SELECT nom, prenom, poste, id, intercontrat FROM personne")
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

        cursor = conn.cursor(buffered=True)

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

def recherche_avec_filtre(id_personne=None, id_competence=None):
    import mysql.connector
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )

    try:
        if id_personne is not None:
            # Recherche par personne
            cursor1 = conn.cursor(buffered=True)
            cursor1.execute("""
                SELECT 
                    personne.id,
                    personne.nom, 
                    personne.prenom, 
                    personne.poste,
                    personne.intercontrat,        
                    hard.competence1, 
                    hard.categorie, 
                    niveau_hard.niveau
                FROM personne
                JOIN niveau_hard ON personne.id = niveau_hard.id_personne
                JOIN hard ON niveau_hard.id_hard = hard.id
                WHERE personne.id = %s
            """, (id_personne,))
            hard_results = cursor1.fetchall()
            cursor1.close()

            cursor2 = conn.cursor(buffered=True)
            cursor2.execute("""
                SELECT 
                    personne.id,
                    personne.nom, 
                    personne.prenom, 
                    personne.poste,
                    personne.intercontrat,  
                    soft.competence2, 
                    niveau_soft.niveau
                FROM personne
                JOIN niveau_soft ON personne.id = niveau_soft.id_personne
                JOIN soft ON niveau_soft.id_soft = soft.id
                WHERE personne.id = %s
            """, (id_personne,))
            soft_results = cursor2.fetchall()
            cursor2.close()

            return {'type': 'personne', 'hard': hard_results, 'soft': soft_results}

        elif id_competence is not None:
            # Recherche par compétence
            cursor3 = conn.cursor(buffered=True)
            cursor3.execute("""
                SELECT 
                    personne.id,
                    personne.nom,
                    personne.prenom,
                    personne.poste,
                    personne.intercontrat,
                    hard.competence1,
                    hard.categorie,
                    niveau_hard.niveau
                FROM niveau_hard
                JOIN hard ON niveau_hard.id_hard = hard.id
                JOIN personne ON niveau_hard.id_personne = personne.id
                WHERE niveau_hard.id_hard = %s
                ORDER BY personne.nom, personne.prenom
            """, (id_competence,))
            results = cursor3.fetchall()
            cursor3.close()
            return {'type': 'competence', 'results': results}

        else:
            return {'type': 'aucun', 'message': 'Aucun identifiant fourni'}

    finally:
        conn.close()



def texte_a_trou(id_personne, chemin_texte="Nom Prenom.txt"):
    # Connexion base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="matrice"
    )
    cursor = conn.cursor(buffered=True)

    # Récupération des données
    cursor.execute("SELECT nom, prenom, poste, intercontrat FROM personne WHERE id = %s", (id_personne,))
    personne = cursor.fetchone()  # (nom, prenom, poste)

    cursor.execute("""
        SELECT hard.competence1, hard.categorie, niveau_hard.niveau
        FROM hard
        JOIN niveau_hard ON hard.id = niveau_hard.id_hard
        WHERE niveau_hard.id_personne = %s
    """, (id_personne,))
    hard_skills = cursor.fetchall()  # liste de tuples

    cursor.execute("""
        SELECT soft.competence2, niveau_soft.niveau
        FROM soft
        JOIN niveau_soft ON soft.id = niveau_soft.id_soft
        WHERE niveau_soft.id_personne = %s
    """, (id_personne,))
    soft_skills = cursor.fetchall()

    conn.close()

    # Lecture du texte à trous
    with open(chemin_texte, 'r', encoding='utf-8') as f:
        texte = f.read()

    # Remplacements
    texte = texte.replace("Nom", personne[0])
    texte = texte.replace("Prenom", personne[1])
    texte = texte.replace("Poste", personne[2])
    texte = texte.replace("Disponibilité", personne[3])

    for i, (comp, cat, niveau) in enumerate(hard_skills):
        texte = texte.replace(f"HardSkill{i+1}", f"{comp} ({cat}) - {niveau}")

    for i, (comp, niveau) in enumerate(soft_skills):
        texte = texte.replace(f"SoftSkill{i+1}", f"{comp} - {niveau}")

    print(texte)

    # Facultatif : écrire dans un nouveau fichier
    #with open("resultat.txt", "w", encoding="utf-8") as f_out:
    #     f_out.write(texte)