#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  leer_fichero.py
import os

fichero=open("C:\\Users\\Usuario\\Desktop\\PYTHON\\Files\\jonathan.txt","w")
fichero.write("Hola soy jonathan como estais?")
fichero.close()


#open the file again 
f=open("C:\\Users\\Usuario\\Desktop\\PYTHON\\Files\\jonathan.txt","rt")
#read its content
print(f.read())
#close the file
f.close()

'''
Nota:si tienes este error es probable que no hayas cerrado el fichero yo como lo he cerrado en la linea 16 me evito ese error
PermissionError: [WinError 32]
El proceso no tiene acceso al archivo porque está siendo utilizado por otro proceso: 'jonathan.txt'
'''
#delete the file from system
if os.path.exists("jonathan.txt"):
  os.remove("jonathan.txt")
else:
  print("The file does not exist")
