import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)


#Classe Connexion
class Connexion:
    def __init__(self, host='localhost', user='root', password='', database='log'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def insert(self, login, mdp):
        sql = "INSERT INTO log (login, mdp) VALUES (%s, %s)"
        self.cursor.execute(sql, (login, mdp))
        self.conn.commit()
    
# Page de login (GET)
@app.route('/')
def login():
    return render_template('login.html')

# Insertion des données (POST)
@app.route('/insert', methods=['POST'])
def insert():
    login = request.form['login']
    mdp = request.form['mdp']

    conn = Connexion()
    conn.insert(login, mdp)

    return render_template('success.html', login=login)
    

#Mise à jour de données (après Insertion dans la base de données)
def update(self):
    self.cursor.execute("UPDATE log SET mdp = %s WHERE login = %s")
    self.cursor.execute(sql, (new_password, login))
    self.conn.commit()

#Lecture de données
def lecture(self):
    self.cursor.execute("SELECT login,mdp from log")

#Suppression de données (on va appuyer sur un bouton au besoin)
def delete(self):
    self.cursor.execute("DELETE FROM log WHERE login =%s AND mdp=%s")