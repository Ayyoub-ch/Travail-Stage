from flask import Flask, render_template, abort
from import_bdd_mysql import get_data  # On importe la fonction que tu viens de définir

app = Flask(__name__)

@app.route("/")
def index():
    try:
        personnes, hard_skills, soft_skills = get_data()  # Appel à la BDD
        return render_template(
            "tableaux.html",  # Le fichier HTML dans /templates/
            personnes=personnes,
            hard_skills=hard_skills,
            soft_skills=soft_skills
        )
    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"An error occurred: {e}")
        # Return a 500 Internal Server Error response
        abort(500, description="An error occurred while fetching data from the database.")

if __name__ == "__main__":
    app.run(debug=True)
