from application import app
from flask import render_template, json, request
import requests


# decorator to access the app
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/trends", methods = ['GET', 'POST'])
def trends():
    date = request.form.get("date")
    topic = request.form.get("topic")
    url = "https://swd-model.herokuapp.com/trends"
    

    if date is None and topic is None:
        response = requests.get(url)
        template="trends.html"
    else:
        input_data = json.dumps({"date": date, "topic": topic})
        response = requests.post(url, input_data)
        template="trendsAndExamples.html"
    
    data = json.loads(response.content.decode("UTF-8"))
    graphJSON = data['graphJSON']
    pos = data['pos']
    neg = data['neg']
    return render_template(template, graphJSON=graphJSON, pos = pos, neg=neg, topic=topic, date=date)


@app.route("/topics", methods = ['GET', 'POST'])
def topics():
    url = "https://swd-model.herokuapp.com/topics"
    response = requests.get(url)
    topics_html = response.content.decode("UTF-8")
    return topics_html

