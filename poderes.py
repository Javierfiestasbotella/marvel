

import os
class Poderes:
    def __init__(self,nombre_poder='',fuerza=None,defensa=None):
        self._nombre_poder=nombre_poder
        self._fuerza=fuerza
        self._defensa=defensa

    @property
    def nombre_poder(self):
        return self._nombre_poder
    @nombre_poder.setter
    def nombre_poder(self,valor):
        self._nombre_poder=valor
    @nombre_poder.deleter
    def nombre_poder(self):
        del self._nombre_poder

    @property
    def fuerza(self):
        return self._fuerza
    @fuerza.setter
    def fuerza(self,valor):
        self._fuerza=valor
    @fuerza.deleter
    def fuerza(self):
        del self._fuerza

    @property
    def defensa(self):
        return self._defensa
    @defensa.setter
    def defensa(self,valor):
        self._defensa=valor
    @defensa.deleter
    def defensa(self):
        del self._defensa

    def __str__(self):
        return f'''
    Nombre del Poder: {self.nombre_poder}
    Fuerza: {self.fuerza} 
    Defensa: {self.defensa}
        ''' 
    

    

