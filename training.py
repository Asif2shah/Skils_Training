from flask import Flask, request, redirect, url_for
from flask import render_template

app = Flask('__name__')

@app.route("/")
def iframe():
    return render_template('iframe.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/onlinereg")
def onlinereg():
    return render_template('onlinereg.html')

@app.route("/media.html")
def media():
    return render_template('media.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/author.html")
def author():
    return render_template('author.html')

@app.route("/about.html")
def about():
    return render_template('about.html')


app.debug = True
app.run()
