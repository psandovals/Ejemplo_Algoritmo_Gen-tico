from random import random
import numpy as np 
import random as rd 

#CLASE PARA REALIZAR EL EJEMPLO DE ALGORITMO GENETICO
class ADN():
    #CONSTRUCTOR DE LA CLASE ADN
    def __init__(self,objetivo, mutacion_velocidad, n_individuos, n_seleccion, n_generaciones, verbose=True): 
        #ATRIBUTOS DE LA CLASE ADN PARA LA CREACION DE INVIDUOS Y POBLACION
        self.objetivo = objetivo
        self.mutacion_velocidad = mutacion_velocidad
        self.n_individuos = n_individuos
        self.n_seleccion = n_seleccion
        self.n_generaciones = n_generaciones
        self.verbose = verbose

    #FUNCION PARA CREAR INDIVIDUOS
    def crear_individuo(self,min=0, max=9):
        individuo = [np.random.randint(min,max) for i in range(len(self.objetivo))]
        
        return individuo

    #FUNCION PARA CREAR POBLACIONES
    def crear_poblacion(self):
        poblacion = [self.crear_individuo() for i in range(self.n_individuos)]
        return poblacion

    #FUNCION PARA LA EVALUACION DE INDIVIDUOS
    def fitness(self, individuo):
        fitness = 0
        for i in range(len(individuo)):
            if individuo[i] == self.objetivo[i]:
                fitness += 1
        return fitness

    #FUNCION PARA REALIZAR SELECCION DE INDIVIDUOS CON MEJOR FITNESS
    def seleccion(self, poblacion):
        punteos = [(self.fitness(i), i) for i in poblacion]
        punteos = [i[1] for i in sorted(punteos)]

        seleccionado = punteos[len(punteos) - self.n_seleccion :]

        return seleccionado


    def reproduccion (self, poblacion, seleccionado):
        puntos = 0
        padre = []

        for i in range (len(poblacion)):
            puntos = np.random.randint(1, len(self.objetivo)- 1)
            padre = rd.sample(seleccionado, 2)

            poblacion[i][:puntos] = padre[0][:puntos]
            poblacion[i][puntos:] = padre[1][puntos:]

        return poblacion

    #FUNCION PARA LA MUTACIÓN DE LA POBLACION
    def mutacion (self, poblacion):
        for i in range(len(poblacion)):
            if rd.random() <= self.mutacion_velocidad:
                puntos = rd.randint(1, len(self.objetivo) -1)
                nuevo_valor = np.random.randint(0, 9)

                while nuevo_valor == poblacion[i][puntos]:
                    nuevo_valor =  np.random.randint(0, 9)
                
                poblacion[i][puntos] = nuevo_valor

        return poblacion

    def corre_genetica(self):
        poblacion = self.crear_poblacion()
        for i in range(self.n_generaciones):
            if self.verbose:
                print('                ')
                print('GENERACION:', i)
                print('POBLACION:' , poblacion )

            seleccion = self.seleccion(poblacion)
            poblacion  = self.reproduccion(poblacion, seleccion)
            poblacion = self.mutacion(poblacion)
    
def main():
        objetivo = [1,0,0,1,0,1,1]
        modelo = ADN(objetivo = objetivo, mutacion_velocidad = 0.20, n_individuos = 15, n_seleccion = 5, n_generaciones = 50, verbose = True )
        modelo.corre_genetica()

if __name__ == '__main__':
    main()
