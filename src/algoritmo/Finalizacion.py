from statistics import mode

class Finalizacion:

    def __init__(self):
        self.porcentaje     = 60    # Criterio de porcentaje ( Criterio 1)
        self.maximo_gen     = 300   # Maximo de generaciones ( Criterio 2)
    
    def verificarCriterio(self, criterio, poblacion, generacion):
        result = None
        if   criterio == 1:
            result = self.criterio1( poblacion, generacion)
        elif criterio == 2:
            result = self.criterio2( poblacion, generacion)
        elif criterio == 3:
            result = self.criterio3( poblacion, generacion)
        return result

    def criterio1(self, poblacion, generacion):
        fin = None
        ordenar_poblacion = poblacion
        ordenar_poblacion = sorted(ordenar_poblacion)
        cont = 1
        lista_fitness = [o.fitness for o in ordenar_poblacion]
        print("lista fitness :", lista_fitness)
        moda_fitness = mode(lista_fitness)
        frecuencia_moda = lista_fitness.count(moda_fitness)
        print("MODA : ",moda_fitness," ::","Frecuencia moda ",frecuencia_moda)


        # Calcular porcentaje de acuerdo a la frecuencia de la moda
        porcentaje = ( frecuencia_moda * 100 ) / len(poblacion)
        print(porcentaje)
        if porcentaje == self.porcentaje:
            print("Finalizo el algoritmo !!!")
            input()

        return fin

    # Cantidad Maxima de generaciones
    def criterio2(self, poblacion, generacion):
        fin = None
        if generacion == self.maximo_gen:
            fin = min(poblacion, key=lambda x: x.fitness)
        return fin
    
    def criterio3(self, poblacion, generacion):
        fin = None

        return fin

    def getCriterio(self, criterio):
        if   criterio == 1:
            return str(self.porcentaje) + "% de la plobacion con valor fitness igual"
        elif criterio == 2:
            return str(self.maximo_gen) + " numero maximo de generaciones"
        return "Retorno de Finalizacion indefinido"


    
