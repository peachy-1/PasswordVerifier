from flask import Flask, render_template, request
from password_verifier import password_strength
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__, template_folder='./templates')
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/password_result', methods = [ 'POST', 'GET' ])
def password_result():
    if request.method == 'POST':
        password = request.form['password']
        result = password_strength(password)
        return render_template('password_result.html', result = result)

@app.route('/email_result', methods = [ 'POST', 'GET' ])
def email_result():
    if request.method == 'POST':
        hibp_key = {'hibp-api-key': '009274fc7df0484a98f9ff01699097a7'}
        email_address = request.form['email']
        response = requests.request('GET', f'https://haveibeenpwned.com/api/v3/breachedaccount/{email_address}', headers = hibp_key)

        if response.status_code !=404:
            results = response.json()
            is_compromised = True
        else:
            results = []
            is_compromised = False

        return render_template('email_result.html', results = results, is_compromised = is_compromised)

if __name__ == '__main__':
    app.run(debug=True)