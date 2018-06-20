from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', resp=None)

@app.route('/handle_get', methods=['POST'])
def handle_get():
    url = request.form['url']
    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
        r = None

    return render_template('home.html', resp=r)
