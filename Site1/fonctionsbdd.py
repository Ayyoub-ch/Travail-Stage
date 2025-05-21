import mysql.connector
from flask import Flask, request, render_template, redirect, url_for

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

@app.route('/login')
def login_page():
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
    # Récupération des identifiants saisis par l'utilisateur dans le formulaire
    login = request.form['login']
    mdp = request.form['mdp']
    # Récupère la valeur du bouton cliqué (connexion ou nouveau)
    action = request.form.get('action')  # plus sûr que ['action']

    # Vérifie que l'action a bien été envoyée, sinon retourne une erreur 400 (mauvaise requête)
    if not action:
        return "Erreur : action manquante", 400

    # Création d'une instance de la classe Connexion pour interagir avec la base de données
    conn = Connexion()

    # Si l'utilisateur a cliqué sur le bouton "Se connecter"
    if action == "connexion":
        if conn.existe(login, mdp):
            # Si l'utilisateur existe dans la base, on affiche une page de succès
            return render_template('success.html', login=login)
        else:
            # Sinon, on affiche une page d'erreur avec redirection automatique
            return render_template('error.html')

    # Si l'utilisateur a cliqué sur le bouton "Nouveau"
    elif action == "nouveau":
        if not conn.existe(login, mdp):
            # Si l'utilisateur n'existe pas encore, on l'insère en base
            conn.insert(login, mdp)
            # Puis on affiche une page de confirmation
            return render_template('success_create.html', login=login)
        else:
             # Si le login existe déjà, on revient au formulaire avec un message d'erreur
            return render_template('login.html', erreur="Cet utilisateur existe déjà.")

    # Si la valeur de l'action est inconnue, retourne une erreur explicite
    else:
        return "Erreur : action inconnue", 400




# Point d'entrée principal
if __name__ == '__main__':
    # ⚠️ Ne pas appeler de méthode ici !
    # ✅ On démarre juste l'application Flask
    app.run(debug=True)