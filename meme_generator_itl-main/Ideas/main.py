from flask import Flask, render_template
import random

app = Flask(__name__)

app.route("/")
def questions():
    domande=["In che anno debuttò Michael Schumacher?", "In che anno è stata creata la F1?"]

    return render_template('index.html', random.choice(domande))
    
def answer1():
    risposte=["1991","1946"]

    return render_template('index.html', (risposte, 0))

def answer2():
    risposte=["1991","1946"] 

    return render_template('index.html', (risposte, 1))

app.run(debug=True)