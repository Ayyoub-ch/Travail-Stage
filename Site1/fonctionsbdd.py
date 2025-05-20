import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)


#Classe Connexion
class Connexion:
    def __init__(self, host='localhost', user='root', password='', database='log'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    #Insertion de données
    @app.route('/insert')
    def insert(self):
        self.cursor.execute("INSERT INTO log (login,mdp) VALUES ($login,$mdp)")
        print("Données insérées avec succès !")
        return render_template('success.html', insert=insert)
    
    

    #Mise à jour de données (après Insertion dans la base de données)
    def update(self):
        self.cursor.execute("UPDATE From log WHERE login")


    #Lecture de données
    def lecture(self):
        self.cursor.execute("SELECT login,mdp from log")

    #Suppression de données (on va appuyer sur un bouton au besoin)
    def delete(self):
        self.cursor.execute("DELETE FROM log WHERE login = $login AND mdp=$mdp")