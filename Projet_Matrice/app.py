from flask import Flask, render_template, abort, redirect, url_for, request, flash
from import_bdd_mysql import get_data, get_personn, recherche_avec_filtre,get_comp,get_all_hard_competences
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
    choix_personne = request.form.get("choix_personne")
    choix_competence = request.form.get("choix_competence")
    intercontrat = 1 if 'intercontrat' in request.form else 0

    print("Choix personne reçu :", repr(choix_personne))
    print("Choix compétence reçu :", repr(choix_competence))
    print("Intercontrat cochée :", intercontrat)

    personnes = get_personn(intercontrat=intercontrat)
    liste_competences = get_all_hard_competences()


    if not choix_personne and not choix_competence:
        return render_template(
            "recherche.html",
            personnes=personnes,
            hard_results=[],
            soft_results=[],
            choix_personne="",
            choix_competence="",
            intercontrat=intercontrat,
            liste_competences=liste_competences
        )

    try:
        if choix_personne:
            id_personne = int(choix_personne)
            results = recherche_avec_filtre(id_personne=id_personne)

            return render_template(
                "recherche.html",
                personnes=personnes,
                hard_results=results.get("hard", []),
                soft_results=results.get("soft", []),
                choix_personne=choix_personne,
                choix_competence="",
                intercontrat=intercontrat,
                liste_competences=liste_competences
            )

        elif choix_competence:
            id_competence = int(choix_competence)
            results = recherche_avec_filtre(id_competence=id_competence)
            hard_skills=get_comp(id_competence)


            hard_results = results.get("results", [])

            if intercontrat == 1:
                hard_results = [res for res in hard_results if res[4] == 1]  # col 4 = intercontrat

            return render_template(
                "recherche.html",
                personnes=personnes,
                hard_results=hard_results,
                soft_results=[],  # pas de soft dans ce cas
                choix_personne="",
                choix_competence=choix_competence,
                intercontrat=intercontrat,
                hard_skills=hard_skills,
                liste_competences=liste_competences
            )

    except (ValueError, TypeError):
        # Cas où l'ID n'est pas un entier valide
        return render_template(
            "recherche.html",
            personnes=personnes,
            hard_results=[],
            soft_results=[],
            choix_personne=choix_personne,
            choix_competence=choix_competence,
            intercontrat=intercontrat,
            liste_competences=liste_competences
        )

    # Fallback
    return render_template(
        "recherche.html",
        personnes=personnes,
        hard_results=[],
        soft_results=[],
        choix_personne="",
        choix_competence="",
        intercontrat=intercontrat,
        liste_competences=liste_competences
    )





"""
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
