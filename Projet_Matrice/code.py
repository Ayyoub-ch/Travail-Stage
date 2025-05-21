import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)



#Classe Connexion
class Connexion:
    def __init__(self, host='localhost', user='root', password='', database='matrice',port=3306):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
        )
        self.cursor = self.conn.cursor()

    #Partie Dev
    def insert_dev(self, nom, prenom):
        sql = "INSERT INTO dev (nom, prenom) VALUES (%s, %s)"
        self.cursor.execute(sql, (nom, prenom))
        self.conn.commit()

    def update_dev(self, new_prenom, nom):
        sql = "UPDATE dev SET nom = %s WHERE prenom = %s"
        self.cursor.execute(sql, (new_prenom, nom))
        self.conn.commit()
    
    def update_dev2(self, new_nom, prenom):
        sql = "UPDATE dev SET prenom = %s WHERE nom = %s"
        self.cursor.execute(sql, (new_nom, prenom))
        self.conn.commit()
    
    def lecture_dev(self):
        self.cursor.execute("SELECT nom, prenom FROM dev")
        return self.cursor.fetchall()
    
    def delete_dev(self, nom, prenom):
        sql = "DELETE FROM dev WHERE nom = %s AND prenom = %s"
        self.cursor.execute(sql, (nom, prenom))
        self.conn.commit()
    
    def existe_dev(self, prenom, nom):
        sql = "SELECT * FROM dev WHERE competence = %s AND acquis = %s"
        self.cursor.execute(sql, (nom, prenom))
        result = self.cursor.fetchone()
        return result is not None

    #Partir Soft Skill
    def insert_soft(self, competence, acquis):
        sql = "INSERT INTO soft (competence, acquis) VALUES (%s, %s)"
        self.cursor.execute(sql, (competence, acquis))
        self.conn.commit()

    
    def update_soft(self, nouvel_acquis, competence):
        sql = "UPDATE soft SET acquis = %s WHERE competence = %s"
        self.cursor.execute(sql, (nouvel_acquis, competence))
        self.conn.commit()
    

    def lecture_soft(self):
        self.cursor.execute("SELECT competence, acquis FROM soft")
        return self.cursor.fetchall()
    
    def delete_soft(self, competence, acquis):
        sql = "DELETE FROM soft WHERE competence = %s AND acquis = %s"
        self.cursor.execute(sql, (competence, acquis))
        self.conn.commit()
    
    def existe_soft(self, competence, acquis):
        sql = "SELECT * FROM soft WHERE competence = %s AND acquis = %s"
        self.cursor.execute(sql, (competence, acquis))
        result = self.cursor.fetchone()
        return result is not None


    #Partir Hard Skill
    def insert_hard(self, competence, niveau):
        sql = "INSERT INTO hard (competence, niveau) VALUES (%s, %s)"
        self.cursor.execute(sql, (competence, niveau))
        self.conn.commit()

    def update_hard(self, new_competence, niveau):
        sql = "UPDATE hard SET niveau = %s WHERE competence = %s"
        self.cursor.execute(sql, (new_competence, niveau))
        self.conn.commit()
    
    def lecture_hard(self):
        self.cursor.execute("SELECT competence, niveau FROM hard")
        return self.cursor.fetchall()

    def delete_hard(self, competence, niveau):
        sql = "DELETE FROM hard WHERE competence = %s AND niveau = %s"
        self.cursor.execute(sql, (competence, niveau))
        self.conn.commit()

    def existe_hard(self, competence, niveau):
        sql = "SELECT * FROM hard WHERE competence = %s AND niveau = %s"
        self.cursor.execute(sql, (competence, niveau))
        result = self.cursor.fetchone()
        return result is not None
    

    
