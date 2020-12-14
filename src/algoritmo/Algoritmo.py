import random
from statistics   import mode
from datetime import datetime
from algoritmo.Finalizacion import *
from algoritmo.Seleccion    import *
class Nodo():
    def __init__(self, solucion, fitness):
        self.solucion = solucion
        self.fitness  = fitness
    
    def __gt__(self, nodo):
        return self.fitness > nodo.fitness

class Algoritmo:
    
    # numPoblacion:     Cantidad de poblacion a manejar para el algoritmo
    # entrada:          Archivo de entrada de notas
    # finalizacion:  Criterio de finalizacion seleccionado por el usuario
    # CriterioPadres:Criterio de Seleccion de Padres seleccionado por un usuario
    def __init__(self, numPoblacion, entrada, finalizacion, criterioPadres, nombre_archivo):
        self.numPoblacion   = numPoblacion
        self.entrada        = entrada
        self.criterioFin    = finalizacion
        self.criterioPadres = criterioPadres
        self.finalizacion   = Finalizacion()
        self.seleccion      = Seleccion()
        self.nombre_archivo = nombre_archivo

    def ejecutar(self):
        print("Generando nuevo modelo ...")
        # Datos Bitacora
        now = datetime.now()
        cadHoraFecha = str(now.hour) + ":" + str(now.minute) + "    " + str(now.day)+"/"+str(now.month)+"/"+str(now.year)

        # Desarrollo del Algoritmo
        generacion = 0
        poblacion  = self.inicializarPoblacion()
        fin = self.finalizacion.verificarCriterio(self.criterioFin, poblacion, generacion)
        
        while fin == None:
            print( generacion)
            padres      = self.seleccion.seleccionarPadres(self.criterioPadres, poblacion)
            poblacion   = self.emparejar(padres, len(poblacion))
            generacion  += 1
            fin = self.finalizacion.verificarCriterio(self.criterioFin, poblacion, generacion)

        # Guardar en bitacora 
        print("Termino el algoritmo ...")
        print(fin.solucion)

        self.registrarBitacora(cadHoraFecha, generacion, fin.solucion, poblacion)

        return fin
    
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
        return int(fitness)
    
    def emparejar(self, padres, total_poblacion):
        nueva_poblacion = padres
        i_inicio = 0
        i_final  = len(padres) - 1 
        for x in range(total_poblacion - len(padres)):
            nueva_poblacion.append( self.cruzar(padres[i_inicio], padres[i_final]))
            i_inicio += 1
            i_final  += 1
        return nueva_poblacion

    def cruzar(self, p1, p2):
        nuevo_hijo = [None] * 4
        padre1 = p1.solucion
        padre2 = p2.solucion
        for i in range(4):
            prob = random.uniform(0,10)
            if prob <= 0.6:
                nuevo_hijo[i] = padre1[i]
            else:
                nuevo_hijo[i] = padre2[i]
        nuevo_hijo = self.mutar(nuevo_hijo)
        hijoNodo = Nodo(
            nuevo_hijo,
            self.evaluarFitness(nuevo_hijo)
        )

        return hijoNodo
    
    def mutar(self, solucion):
        mutado = solucion
        hayMutar = random.randint(0, 1)
        if hayMutar == 1:
            for i in range(len(mutado)):
                hayMutar = random.randint(0, 1)
                if hayMutar == 1:
                    mutado[i] = random.uniform(-2, 2)
        return mutado


    def imprimirPoblacion(self, poblacion):
        for nodo in poblacion:
            print(nodo.solucion)
    
    def registrarBitacora(self, horaFecha, total_generacion, solucion, poblacion):
        cad_registro = "*" * 15 + "\n"
        cad_registro += "FECHA Y HORA : " + horaFecha + "\n"
        cad_registro += "NUMERO POBLACION       :" + str(len(poblacion)) + "\n"
        cad_registro += "DOCUMENTO    : " + self.nombre_archivo + "\n"
        cad_registro += "Criterion Finalizacion :" + self.finalizacion.getCriterio(self.criterioFin) + "\n"
        cad_registro += "Criterio  Seleccion    :" + self.seleccion.getSeleccion(self.criterioPadres) + "\n"
        cad_registro += "GENERACIONES GENERADAS :" + str(total_generacion) + "\n"
        cad_registro += "MODELO SOLUCION ==> " + "NC = ({})P1 + ({})P2 + ({})P3 + ({})P4".format(solucion[0], solucion[1], solucion[2], solucion[3]) + "\n"
        f = open('bitacora.txt', 'a')
        f.write('\n' + cad_registro + '\n')
        f.close()
        
