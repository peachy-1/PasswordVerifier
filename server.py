from flask import Flask, render_template, request
from password_verifier import password_strength
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='./templates')
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result', methods = [ 'POST', 'GET' ])
def result():
    if request.method == 'POST':
        password = request.form['password']
        result = password_strength(password)
        return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)