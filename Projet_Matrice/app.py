from flask import Flask, render_template, abort, redirect, url_for, request
from import_bdd_mysql import get_data, get_personn, recherche
import import_excel_all

app = Flask(__name__)

@app.route("/")
def index():
    try:
        personne=get_personn()
        return render_template(
            "admin.html",personne=personne
        )
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        abort(500, description="An error occurred while fetching data from the database.")

@app.route('/importer', methods=['POST'])
def importer_matrice():
    try:
        import_excel_all.run()  # nouvelle méthode centralisée
        return redirect(url_for('index'))
    except Exception as e:
        app.logger.error(f"Erreur lors de l'importation : {e}")
        abort(500, description="Erreur lors de l'importation des matrices.")



@app.route('/voir_comp', methods=['POST'])
def voir_comp():
    try:
        personnes, hard_skills, soft_skills = get_data()
        return render_template(
            "tableaux.html",
            personnes=personnes,
            hard_skills=hard_skills,
            soft_skills=soft_skills)
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        abort(500, description="An error occurred while fetching data from the database.")

@app.route('/retour', methods=['POST'])
def retour():
    return render_template("admin.html")


@app.route('/rechercher', methods=['POST'])
def rechercher():
    recherche = recherche()
    return render_template(
            "recherche.html",
            recherche=recherche)

if __name__ == "__main__":
    app.run(debug=True)
