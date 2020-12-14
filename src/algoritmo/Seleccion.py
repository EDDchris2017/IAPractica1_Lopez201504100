class Seleccion:

    def __init__(self):
        self.porcentaje_padres = 60 # Porcentaje de la poblacion a considerar para seleccion de padres
    
    #Seleccion de los padres con mejor valor Fitness
    def seleccionarPadres(self, seleccion, poblacion):
        mejores_padres = []
        if seleccion == 1:
            mejores_padres = self.seleccion1(poblacion)
        elif seleccion == 2:
            mejores_padres = self.seleccion2(poblacion)
        elif seleccion == 3:
            mejores_padres = self.seleccion3(poblacion)
        
        return mejores_padres
    
    def seleccion1(self, poblacion):
        print ("Seleccion de los mejores padres de la poblacion ")
        mejores_padres = []
        padres_considerar = int(self.porcentaje_padres * len(poblacion) / 100)
        mejores_padres = sorted(poblacion)[:padres_considerar]

        return mejores_padres

    def seleccion2(self, poblacion):
        mejores_padres = []

        return mejores_padres
    
    def seleccion3(self, poblacion):
        mejores_padres = []

        return mejores_padres
    
    def getSeleccion(self, seleccion):
        if seleccion == 1:
            return "Seleccion de padres como el mejor valor fitness => " + str(self.porcentaje_padres) + "% padres seleccionados"
        return "Seleccion indefinida"