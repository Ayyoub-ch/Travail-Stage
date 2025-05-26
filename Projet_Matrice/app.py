from flask import Flask, render_template, abort
from import_bdd_mysql import get_data  # doit retourner 5 éléments

app = Flask(__name__)

@app.route("/")
def index():
    try:
        personnes, hard_skills, soft_skills, niveaux_hard, niveaux_soft = get_data()  # 🆕
        return render_template(
            "tableaux.html",
            personnes=personnes,
            hard_skills=hard_skills,
            soft_skills=soft_skills,
            niveaux_hard=niveaux_hard,  # 🆕
            niveaux_soft=niveaux_soft   # 🆕
        )
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        abort(500, description="An error occurred while fetching data from the database.")

if __name__ == "__main__":
    app.run(debug=True)
