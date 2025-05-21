import pandas as pd

import mysql.connector

from flask import Flask, request, render_template

app = Flask(__name__)



#Classe Matrice
class Matrice:
    def __init__(self, host='localhost', user='root', password='', database='matrice',port=3306):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
        )
        self.cursor = self.conn.cursor()

    #Partie Personne
    def insert_dev(self, nom, prenom):
        sql = "INSERT INTO personne (nom, prenom) VALUES (%s, %s)"
        self.cursor.execute(sql, (nom, prenom))
        self.conn.commit()

    def update_dev(self, new_prenom, nom):
        sql = "UPDATE personne SET nom = %s WHERE prenom = %s"
        self.cursor.execute(sql, (new_prenom, nom))
        self.conn.commit()
    
    def update_dev2(self, new_nom, prenom):
        sql = "UPDATE personne SET prenom = %s WHERE nom = %s"
        self.cursor.execute(sql, (new_nom, prenom))
        self.conn.commit()
    
    def lecture_dev(self):
        self.cursor.execute("SELECT nom, prenom FROM personne")
        return self.cursor.fetchall()
    
    def delete_dev(self, nom, prenom):
        sql = "DELETE FROM personne WHERE nom = %s AND prenom = %s"
        self.cursor.execute(sql, (nom, prenom))
        self.conn.commit()
    
    def existe_dev(self, prenom, nom):
        sql = "SELECT * FROM personne WHERE nom = %s AND prenom = %s"
        self.cursor.execute(sql, (nom, prenom))
        result = self.cursor.fetchone()
        return result is not None

    #Partir Soft Skill
    def insert_soft(self, competence2, acquis):
        sql = "INSERT INTO soft (competence2, acquis) VALUES (%s, %s)"
        self.cursor.execute(sql, (competence2, acquis))
        self.conn.commit()

    
    def update_soft(self, nouvel_acquis, competence2):
        sql = "UPDATE soft SET acquis = %s WHERE competence2 = %s"
        self.cursor.execute(sql, (nouvel_acquis, competence2))
        self.conn.commit()
    

    def lecture_soft(self):
        self.cursor.execute("SELECT competence2, acquis FROM soft")
        return self.cursor.fetchall()
    
    def delete_soft(self, competence2, acquis):
        sql = "DELETE FROM soft WHERE competence2 = %s AND acquis = %s"
        self.cursor.execute(sql, (competence2, acquis))
        self.conn.commit()
    
    def existe_soft(self, competence2, acquis):
        sql = "SELECT * FROM soft WHERE competence2 = %s AND acquis = %s"
        self.cursor.execute(sql, (competence2, acquis))
        result = self.cursor.fetchone()
        return result is not None


    #Partir Hard Skill
    def insert_hard(self, competence1, niveau):
        sql = "INSERT INTO hard (competence1, niveau) VALUES (%s, %s)"
        self.cursor.execute(sql, (competence1, niveau))
        self.conn.commit()

    def update_hard(self, new_competence, niveau):
        sql = "UPDATE hard SET niveau = %s WHERE competence1 = %s"
        self.cursor.execute(sql, (new_competence, niveau))
        self.conn.commit()
    
    def lecture_hard(self):
        self.cursor.execute("SELECT competence1, niveau FROM hard")
        return self.cursor.fetchall()

    def delete_hard(self, competence1, niveau):
        sql = "DELETE FROM hard WHERE competence1 = %s AND niveau = %s"
        self.cursor.execute(sql, (competence1, niveau))
        self.conn.commit()

    def existe_hard(self, competence1, niveau):
        sql = "SELECT * FROM hard WHERE competence1 = %s AND niveau = %s"
        self.cursor.execute(sql, (competence1, niveau))
        result = self.cursor.fetchone()
        return result is not None
    

    
@app.route('/')
def debut():
    return render_template('tableau.html')

# Insertion des données (POST)
@app.route('/insert', methods=['POST'])
def insert():
    nom= request.form['nom']
    prenom = request.form['prenom']
    competence1 = request.form['competence1']
    niveau = request.form['niveau']
    competence2 = request.form['competence2']
    acquis = request.form['acquis']

    conn = Matrice()
    conn.insert_soft(competence1, niveau)
    conn.insert_hard(competence2, acquis)
    conn.insert_dev(nom, prenom)

    return render_template('tableau.html')





# Point d'entrée principal
if __name__ == '__main__':
    # ⚠️ Ne pas appeler de méthode ici !
    # ✅ On démarre juste l'application Flask
    app.run(debug=True)