from flask import Flask, render_template, abort, redirect, url_for, request
from import_bdd_mysql import get_data
import import_excel_soft  # ⚠️ Ce module doit avoir une fonction `run()` définie
import import_excel_hard  # ⚠️ Ce module doit avoir une fonction `run()` définie

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return render_template(
            "admin.html"
        )
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        abort(500, description="An error occurred while fetching data from the database.")

@app.route('/importer', methods=['POST'])
def importer_matrice():
    try:
        import_excel_soft.run()  # Cette fonction doit exécuter l’importation
        import_excel_hard.run()  # Cette fonction doit exécuter l’importation
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

if __name__ == "__main__":
    app.run(debug=True)

