import csv
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
from algoritmo.Algoritmo import *
import json
#Se leventa en puerto 5000 !!!
app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route("/generar", methods=['GET', 'POST'])
def ejecutarModelo():
    if request.method == 'POST':
        poblacion_form      = int(request.form['poblacion'])
        finalizacion_form   = int(request.form['finalizacion'])
        seleccion_form      = int(request.form['padres'])
        f = request.files['file']
        # Leer contenido del CSV
        f.save(f.filename)
        archivo = open(f.filename)
        contenido = list(csv.reader(archivo,delimiter=','))
        # Iniciar algoritmo
        algoritmo = Algoritmo(poblacion_form, contenido, finalizacion_form, seleccion_form, f.filename)
        fin = algoritmo.ejecutar()
        session['modelo'] = fin.solucion

        return render_template("index.html", modelo = fin.solucion)
    #algoritmo =  Algoritmo(6, 1, 2)
    #algoritmo.ejecutar()
    return "Error al recibir datos"
   
@app.route("/mensaje", methods=['GET', 'POST'])
def mensaje():
    print("Datos de Formulario")
    if request.method == 'POST':
        poblacion_form = request.form['poblacion']
        finalizacion_form   = request.form['finalizacion']
        seleccion_form      = request.form['padres']
        print(poblacion_form)
        print(finalizacion_form)
        print(seleccion_form)
    return render_template("index.html")

@app.route("/evaluar", methods=['POST'])
def evaluar():
    if request.method == "POST":
        print("Evaluando modelo")
        if request.method == 'POST':
            modelo = session.get('modelo')
            print(modelo)
            if modelo != None:
                p1 = float(request.form["p1"])
                p2 = float(request.form["p2"])
                p3 = float(request.form["p3"])
                p4 = float(request.form["p4"])
                res_modelo = modelo[0] * p1 + modelo[1] * p2 + modelo[2] * p3 + modelo[3] * p4
                return render_template("index.html", modelo = modelo, res = res_modelo)
            else:
                print("No existe modelo")
                return render_template("index.html", modelo = 0, res = "")
    return render_template("index.html", modelo = 0, res = "")
    

@app.route('/status')
def verificar():
   return 'Aplicacion Practica 1 IA ACTIVO'

@app.route('/')
def home_form():
    return render_template("index.html", modelo= 0, res = "")


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)



