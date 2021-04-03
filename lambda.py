#!/usr/bin/env python
# -*- coding: utf-8 -*-
while(True):
	primero=int(input("Introduce el primer numero "))
	segundo=int(input("Introduce el segundo numero "))
	
	decision=input("Que operacion quieres hacer? \n Suma=S \n Resta=R \n Multiplicar=M \n Division=D \n X=salir")
	
	if decision.__eq__("S") or decision.__eq__("s"):
			suma=lambda variable,variable2:variable + variable2 #es una alternativa a los "def"
			print(suma(primero,segundo))
	elif decision.__eq__("R") or decision.__eq__("r"):
			restar=lambda variable,variable2:variable - variable2 #es una alternativa a los "def"
			print(restar(primero,segundo))
	elif decision.__eq__("M") or decision.__eq__("m"):
			multiplicar=lambda variable,variable2:variable * variable2 #es una alternativa a los "def"
			print(multiplicar(primero,segundo))
	elif decision.__eq__("D") or decision.__eq__("d"):
			division=lambda variable,variable2:variable / variable2 #es una alternativa a los "def"
			print(division(primero,segundo))		
	elif decision.__eq__("X") or decision.__eq__("x"):
			break		



'''
el simbolo : equivale a return de una funcion normal
'''
