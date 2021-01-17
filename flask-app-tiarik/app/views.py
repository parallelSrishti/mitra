# views.py

from flask import render_template
from train.train_model import train_model_results

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")
