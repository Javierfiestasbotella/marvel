from re import S, X
from poderes import Poderes
import os
class Superheroes:
    def __init__(self,name='',nivel=None):
        self._name=name
        self._nivel=nivel
        self._poderes={}

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,valor):
        self._name=valor
    @name.deleter
    def name(self):
        del self._name

    @property
    def nivel(self):
        return self._nivel
    @nivel.setter
    def nivel(self,valor):
        self._nivel=valor
    @nivel.deleter
    def nivel(self):
        del self._nivel

    @property
    def poderes(self):
        return self._poderes
    @poderes.setter
    def poderes(self,valor):
        self._poderes=valor
    @poderes.deleter
    def poderes(self):
        del self._poderes

    def __str__(self):
            return f'''
    Nombre: {self.name}
    Nivel: {self.nivel} 
    Poderes: {self.poderes}
            ''' 
    
    
    def insertar_poderes_en_lista(self):
        continuar=True
        while continuar:
            os.system('cls')
            poder_nuevo=input('Introduzaca el nuevo poder: ')
            while (fuerza := int(input("Ingrese el nivel de Fuerza en un rango de 1 a 13 : "))) not in range(1,14):  pass
            while (defensa := int(input("Ingrese el nivel de Defensa en un rango de 1 a 13 : "))) not in range(1,14):  pass
            poderes2=Poderes(poder_nuevo,fuerza,defensa)
            #print(poderes2)
            self.poderes[poder_nuevo]=[fuerza,defensa]
            seguir=input('¿Quieres añadir más poderes? (s/n) ')
            if seguir.lower()!='s':
                continuar=False



x=Superheroes('Superman',3)
x.insertar_poderes_en_lista()
print(x)


