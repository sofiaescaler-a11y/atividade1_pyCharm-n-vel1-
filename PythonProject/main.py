

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('calculadora.html')

@app.route('/calcular_Idade', methods=['POST'])
def calcular_Idade():
    data_nasc = float(request.form['data_nasc'])
    idade = 2026 - data_nasc

    return render_template('calculadora.html', idade = idade)

if __name__ == '__main__':
    app.run(debug=True)