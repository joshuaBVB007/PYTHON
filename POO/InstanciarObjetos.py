#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Alumno.py

class Persona:
	def __init__(self,nombre,edad):
		self.nombre=nombre
		self.edad=edad	
		
	def dimenombre(self):
		print("El nombre es: ",self.nombre)	
	
	def dimeEdad(self):
		print("La edad es: ",self.edad)	
			
						
#creamos un objeto
var=Persona("Jonathan",20)
#imprimimos la edad en principio es 20
var.dimeEdad()
#cambiamos la edad a 100
var.edad=100
var.dimeEdad()
#Eliminamos la propiedad edad
del var.edad
#Nos da una exception al haber borrado una propiedad
var.dimeEdad()

