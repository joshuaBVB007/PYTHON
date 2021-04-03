#!/usr/bin/env python
# -*- coding: utf-8 -*-

#creamos una tupla con parentesis.
t=("jonathan","calderon","ascencio","josael")
#Nota Importante los valores de las tuples no se pueden cambiar son inmutables


#posible solucion es convertir la tuple en lista y cambiar el indice

x=list(t)#Hemos convertido la  tupla en lista
x[1]="pedro"#hemos modificado el valor[1] de la lista
t=tuple(x) #hemos convertido una lista en tupla 
print(t)# imprimimos la tupla
