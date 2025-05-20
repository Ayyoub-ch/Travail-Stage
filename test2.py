from flask import Flask, render_template,request
import datetime

app=Flask(__name__)

@app.route('/')
def test():
    return render_template('bonjour.html')

liste_perso=[
    {'prenom':'Goku', 'race':'Saiyan','puissance':50},
    {'prenom':'Vegeta', 'race':'Saiyan' ,'puissance':50},
    {'prenom':'Trunks', 'race':'Hybrid' ,'puissance':45},
    {'prenom':'Boo', 'race':'Majin' ,'puissance':70},
    {'prenom':'Piccolo', 'race':'Namek' ,'puissance':40}
]

@app.route('/perso')
def perso():
    classe=(request.args.get('c'))
    return render_template('perso.html',perso=liste_perso)