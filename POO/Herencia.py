#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Herencia.py


class Persona:
	def __init__(self,Nombre,Edad):
		self.nom=Nombre
		self.edad=Edad
	
	def dimedatosPersona(self):
		print("El nombre es",self.nom)


'''en python heredas tanto métodos como constructor de la superclase
eso explica que studiante esté utilizando un constructor similar 
al de Persona cuando no esta definido asi en STUDIANTE y que ademas utilice un metodo definido en Persona'''

class Studiante(Persona):
	#pass
	'''Que pasa si borramos pass y le agregamos un metodo init() a esta clase? No volverá a utilizar la funcion init del padre(Persona)
	y tendriamos que comentar la palabra pass de la linea 21 o eliminarla de nuestro codigo'''
	def __init__(self,nombre):
		self.nom=nombre 

x=Persona("Jonathan",26)
x.dimedatosPersona()
y=Studiante("Jona")
y.dimedatosPersona()
