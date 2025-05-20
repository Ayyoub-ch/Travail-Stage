from flask import Flask, render_template
import datetime

app=Flask(__name__)

@app.route('/')
def test():
    return render_template('bonjour.html')

@app.route('/heure')
def heure():
    date_heure=datetime.datetime.now()
    h=date_heure.hour
    m=date_heure.minute
    s=date_heure.second
    print(h,m,s)
    return render_template('hour.html',heure=h,minute=m,second=s)