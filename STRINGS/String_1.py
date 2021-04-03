#!/usr/bin/env python
# -*- coding: utf-8 -*-


prefix=input("Introduce la letra a buscar en la frase: ")
f="Guido Van Rossum"
imprimir="el caracter {} aparece en la frase \"Guido Van Rossum\""


if prefix in f:
	print(imprimir.format(prefix))
else:
	print("el caracter no aparece en la frase ")
