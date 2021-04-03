#!/usr/bin/env python
# -*- coding: utf-8 -*-

f=input("Introduce una frase: ")
a="a"
contador=0
for i in f:
	print(i)
	if a.__eq__(i.lower()) or a.__eq__(i.upper()):
		contador+=1 
print("la frase contiene ",contador,"\"a\"")
