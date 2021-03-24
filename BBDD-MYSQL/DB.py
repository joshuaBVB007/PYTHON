#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DB.py

'''Nota importante 
es necesario descargar el driver(Los comandos que te dejo abajo son de Windows)

actualizamos primero
python.exe -m pip install --upgrade pip

instalamos driver
python -m pip install mysql-connector-python

'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jaKsVaFa7",
  database="bd_python"
)

print(mydb)

#necesito buscar informacion del porque necesito un cursor para crear la BBDD
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE BD_PYTHON")
#mycursor.execute("CREATE TABLE Personas (Nombre VARCHAR(255), Edad VARCHAR(255))")

while True:
	print("Gestion Joan D'austria")
	decision=int(input("1-INSERT\n2-DELETE\n3-UPDATE\n4-SELECT\n5-Terminar"))

	if decision==1:
			sql = "INSERT INTO personas (Nombre, Edad) VALUES (%s, %s)"
			Nombre_persona=input("Nombre?")
			Edad_persona=input("Edad?")
			val = (Nombre_persona,Edad_persona)
			mycursor.execute(sql, val)
			#con el commit ejecutamos el insert
			mydb.commit()
			print(mycursor.rowcount, "record inserted.")
	elif decision==2:
			print("Borrar Alumno")
			Nombre_persona=input("Nombre?")
			sql = "DELETE FROM personas WHERE Nombre = '"+Nombre_persona+"'"
			print(sql)
			val=(Nombre_persona)
			mycursor.execute(sql,val)
			mydb.commit()
			print(mycursor.rowcount, "record(s) deleted")
	elif decision==3:
			print("Actualizar Alumno") 
			Nombre_persona=input("Nombre nuevo?")
			Nombre_viejo=input("Nombre viejo?")
			sql = "UPDATE personas SET Nombre = '"+Nombre_persona+"' WHERE Nombre = '"+Nombre_viejo+"'"
			mycursor.execute(sql)
			mydb.commit()
			print(mycursor.rowcount, "record(s) affected")
	elif decision==4:
			mycursor.execute("SELECT * FROM personas")
			myresult = mycursor.fetchall()
			for x in myresult:
				print(x)		
	elif decision==5:
			print("Hemos terminado")
			break
