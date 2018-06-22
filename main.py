from flask import Flask, render_template, request, abort, jsonify, redirect
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', resp=None)

@app.route('/api')
def api():
    return jsonify({'name': 'etf', 'version': '0.01'})

@app.route('/error')
def error():
    codes = [404, 401, 403, 500]
    random.shuffle(codes)
    abort(codes[0])

@app.route('/handle_get', methods=['POST'])
def handle_get():
    url = request.form['url']
    assertion = request.form['assert']
    assertion_success = None
    try:
        r = requests.get(url)
        if assertion is not None and assertion != '':
            obj = r.json()
            if assertion:
                assertion_success = eval(assertion)
    except Exception as e:
        print(e)
        r = None

    resp = build_resp(r)
    resp['assertion'] = assertion
    resp['assertion_success'] = assertion_success

    return render_template('home.html', resp=resp)

def build_resp(r):
    resp = {'success': False}
    if r is None:
        return resp

    if r.status_code < 400:
        resp['success'] = True

    resp['url'] = r.url
    resp['text'] = r.text
    resp['headers'] = r.headers
    resp['status_code'] = r.status_code

    return resp
