from flask import Flask, render_template, abort, redirect, url_for, request, flash
from import_bdd_mysql import get_data, get_personn, recherche# get_all_categories, get_filtered_skills
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
        import_excel_all.run()  # ta fonction d'import
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
    choix = request.form.get("choix")
    print("🔘 Choix reçu :", repr(choix), "| type:", type(choix))

    personnes = get_personn()

     # Si l'utilisateur n'a rien sélectionné, on prend par défaut la première personne
    if not choix and personnes:
        choix = str(personnes[0][2])  # p[2] = id de la première personne
        print("ℹ️ Choix forcé sur le premier ID :", choix)

    try:
        choix_int = int(choix)
    except (ValueError, TypeError):
        return render_template(
            "recherche.html",
            personnes=personnes,
            hard_results=[],
            soft_results=[],
            choix=""
        )

    hard_results, soft_results = recherche(choix)

    return render_template(
        "recherche.html",
        personnes=personnes,
        hard_results=hard_results,
        soft_results=soft_results,
        choix=choix
    )
""""
@app.route('/filtrage', methods=['GET', 'POST'])
def filtrer():
    categories = get_all_categories()

    if request.method == 'POST':
        selected = request.form.getlist('categories')
        filtered_skills = get_filtered_skills(selected)
    else:
        filtered_skills = get_filtered_skills()

    return render_template('recherche.html', categories=categories, filtered_skills=filtered_skills)


"""



if __name__ == "__main__":
    app.run(debug=True)
