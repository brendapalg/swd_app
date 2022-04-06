from application import app
from flask import render_template, request, json, jsonify
import requests
import numpy
import pandas


# decorator to access the app
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/trends", methods = ['GET', 'POST'])
def trends():
    url = "http://127.0.0.1:5000/trends"
    response = requests.get(url)
    graphJSON = response.content.decode("UTF-8")
    return render_template("trends.html", graphJSON=graphJSON)


@app.route("/topics", methods = ['GET', 'POST'])
def topics():
    url = "http://127.0.0.1:5000/topics"
    response = requests.get(url)
    topics_html = response.content.decode("UTF-8")
    return topics_html

