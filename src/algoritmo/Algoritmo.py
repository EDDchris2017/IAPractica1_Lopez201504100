import random
import Finalizacion

class Nodo:
    def __init__(self, solucion, fitness):
        self.solucion = solucion
        self.fitness  = fitness

class Algoritmo:
    
    # numPoblacion:     Cantidad de poblacion a manejar para el algoritmo
    # entrada:          Archivo de entrada de notas
    # finalizacion:  Criterio de finalizacion seleccionado por el usuario
    # CriterioPadres:Criterio de Seleccion de Padres seleccionado por un usuario
    def __init__(self, numPoblacion, entrada, finalizacion, criterioPadres):
        self.numPoblacion = numPoblacion
        self.entrada      = entrada
        self.finalizacion = finalizacion
        self.criterioPadres = criterioPadres

    def ejecutar(self):
        print("Generando nuevo modelo ...")
        generacion = 0
        poblacion  = self.inicializarPoblacion()
        #self.imprimirPoblacion(poblacion)
    
    def inicializarPoblacion(self):
        poblacion = []
        for i in range(self.numPoblacion):
             poblacion.append(self.crearIndividuo())

        return poblacion

    def crearIndividuo(self):
        solucion = []
        for i in range(4):
            solucion.append(random.uniform(-2, 2)) # Rango de datos aleatorios de Individuo
        nuevo_nodo = Nodo(
            solucion,
            self. evaluarFitness(solucion)
        )
        return nuevo_nodo
    
    def evaluarFitness(self, solucion):
        # Recorrer contenido del archivo
        fitness = 0
        # e(NRi - NCi)^2
        total_promedio = 0
        encabezado = True
        tam = 0
        for notas in self.entrada:
            if not(encabezado):
                tam += 1
                nota_estimada = solucion[0]*float(notas[0]) + solucion[1]*float(notas[1]) + solucion[2]*float(notas[2]) + solucion[3]*float(notas[3])
                total_promedio += (float(notas[4]) - nota_estimada)*(float(notas[4]) - nota_estimada)
            else:
                encabezado = False
        fitness = (1/tam)*(total_promedio)
        return fitness
    
    def imprimirPoblacion(self, poblacion):
        for nodo in poblacion:
            print(nodo.solucion)
        
