#!/usr/bin/python
# -*- coding: utf-8 -*-
# Marcio de Lima - Case Santander
# Front-End com flask

# Imports
from flask import Flask, request
from flask import render_template
from tools.heart import Heart
import json

# Cria a app
app = Flask(__name__)

# Home Page
@app.route("/")
def index():
    result = None
    return render_template("index.html", result = result, probabilidade=None, msg=None)

# Página com o resultado da previsão
@app.route("/verificar", methods = ["POST"])
def verificar():

    values = request.form.getlist('new_heart')
    heart = Heart(values)
    value_to_predict = heart.prepare()
    result = heart.predict(value_to_predict)
    
    #ARRUMAR LOGICA DE APRESENTACAO DO MODELO - RESULTADO S/N, PROBABILIDADE
    prob = "%.2f" % (float(result.get('probabilidade')) * 100.0)
    result = int(result.get('resultado'))
    if (result == 0):
    	result = 'Não há indícios de doença'
    	prob = None
    else:
    	result = 'Encontrado indícios de doença'
    mensagem = "Atenção, esse resultado é uma previsão, sempre procure um médico cardiologista."
    
    return render_template('index.html', result = result, probabilidade=prob, msg=mensagem)

# Executa a app
if __name__ == "__main__":
    app.run(port = 5000 , host='0.0.0.0', debug = True)

