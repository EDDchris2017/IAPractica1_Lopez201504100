import csv
from flask import Flask, render_template, request
from algoritmo.Algoritmo import *
import json
#Se leventa en puerto 5000 !!!
app = Flask(__name__)

@app.route("/generar", methods=['GET', 'POST'])
def ejecutarModelo():
    if request.method == 'POST':
        f = request.files['file']
        # Leer contenido del CSV
        f.save(f.filename)
        archivo = open(f.filename)
        contenido = list(csv.reader(archivo,delimiter=','))
        # Iniciar algoritmo
        algoritmo = Algoritmo(6, contenido, 1, 2)
        algoritmo.ejecutar()

        return 'Archivo cargado de manera exitosa'
    #algoritmo =  Algoritmo(6, 1, 2)
    #algoritmo.ejecutar()
    return "Error al recibir datos"
   

@app.route('/status')
def verificar():
   return 'Aplicacion Practica 1 IA ACTIVO'

@app.route('/')
def home_form():
    return render_template("index.html")


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)



