from flask import Flask, render_template
from random import randint
from time import time

from helpers.numbers_api import get_fact_for_number

app = Flask(__name__)


@app.route("/")
def homepage():
    current_epoch = time()
    random_number = randint(0, 10000)

    return render_template("homepage.html", number=random_number, time=current_epoch)


@app.route("/number-fact")
def number_fact():
    random_number = randint(0, 100)
    fact = get_fact_for_number(random_number)

    return render_template("number-fact.html", number=random_number, fact=fact)
