#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lista_aleatoria.py
import random

#creamos una lista con 100 elementos
lista=[]
for i in range(100):
	lista.append(random.random())
#imprimimos los numeros aleatorios
lista_ordenada=sorted(lista)
for j in lista_ordenada:
	print(j)
