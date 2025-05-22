import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Classe Matrice
class Matrice:
    def __init__(self, host='localhost', user='root', password='', database='matrice', port=3306):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
        )
        self.cursor = self.conn.cursor()

    # Méthode pour insérer des données depuis un DataFrame
    def insert_from_dataframe(self, df, table_name):
        engine = create_engine('mysql+pymysql://root:@localhost/matrice')
        df.to_sql(table_name, engine, if_exists='append', index=False)

    # Autres méthodes de la classe Matrice...
    # (Vos méthodes existantes pour insert_personne, update_personne, etc.)

@app.route('/')
def debut():
    return render_template('tableau.html')

# Insertion des données (POST)
@app.route('/insert', methods=['POST'])
def insert():
    nom = request.form['nom']
    prenom = request.form['prenom']
    poste = request.form['poste']
    competence1 = request.form['competence1']
    categorie = request.form['niveau']
    competence2 = request.form['competence2']

    conn = Matrice()
    conn.insert_soft(competence2)
    conn.insert_hard(competence1, categorie)
    conn.insert_personne(nom, prenom, poste)

    return render_template('tableau.html')

# Importation des données depuis un fichier Excel
@app.route('/import_excel', methods=['POST'])
def import_excel():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        df_personne = pd.read_excel(file, sheet_name='personne', engine='openpyxl')
        df_hard = pd.read_excel(file, sheet_name='hard', engine='openpyxl')
        df_soft = pd.read_excel(file, sheet_name='soft', engine='openpyxl')

        conn = Matrice()
        conn.insert_from_dataframe(df_personne, 'personne')
        conn.insert_from_dataframe(df_hard, 'hard')
        conn.insert_from_dataframe(df_soft, 'soft')

        return "Data imported successfully", 200

# Point d'entrée principal
if __name__ == '__main__':
    app.run(debug=True)
