from application import app
from flask import render_template, request, json, jsonify
import requests
import numpy
import pandas


# decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    url = "http://127.0.0.1:5000/api"
    response = requests.get(url)
    graphJSON = response.content.decode("UTF-8")
    return render_template("index.html", graphJSON=graphJSON)


# @app.route("/trends", methods = ['GET', 'POST'])
# def trends():
#     data = {}
#     #data['date'] = request.form.get("selected_date")
#     #data_dict = json.dumps(data)

#     return render_template("index.html" )

