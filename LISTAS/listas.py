#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  listas.py

lista=[]
while True:
	nombre=int(input("Que quieres hacer\n 1-Agregar un nombre\n 2-Eliminar un nombre\n 3-Imprimir lista\n 4-Terminar "))
	
	if nombre==1:
		nombre=input("Dime nombre a agregar ")
		lista.append(nombre)
	elif nombre==2:
		nombre=input("Dime nombre a eliminar ")
		lista.remove(nombre)
	elif nombre==3:
		print("La lista es: ")
		[print(i)for i in lista]	
	else:
		print("Hemos terminado ")
		break			
	
