import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)


#Classe Connexion
class Connexion:
    def __init__(self, host='localhost', user='root', password='', database='log',port=3306):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
        )
        self.cursor = self.conn.cursor()

    def insert(self, login, mdp):
        sql = "INSERT INTO connexion (login, mdp) VALUES (%s, %s)"
        self.cursor.execute(sql, (login, mdp))
        self.conn.commit()

    def update(self, new_password, login):
        sql = "UPDATE connexion SET mdp = %s WHERE login = %s"
        self.cursor.execute(sql, (new_password, login))
        self.conn.commit()

    def lecture(self):
        self.cursor.execute("SELECT login, mdp FROM connexion")
        return self.cursor.fetchall()

    def delete(self, login, mdp):
        sql = "DELETE FROM connexion WHERE login = %s AND mdp = %s"
        self.cursor.execute(sql, (login, mdp))
        self.conn.commit()
    
    def existe(self, login, mdp):
        sql = "SELECT * FROM connexion WHERE login = %s AND mdp = %s"
        self.cursor.execute(sql, (login, mdp))
        result = self.cursor.fetchone()
        return result is not None
    
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

@app.route('/verifier', methods=['POST'])
def verifier():
    login = request.form['login']
    mdp = request.form['mdp']

    conn = Connexion()
    if conn.existe(login, mdp):
        return render_template('success.html', login=login)
    else:
        conn.insert(login, mdp)
        return render_template('creation_utilisateur.html')


# Point d'entrée principal
if __name__ == '__main__':
    # ⚠️ Ne pas appeler de méthode ici !
    # ✅ On démarre juste l'application Flask
    app.run(debug=True)