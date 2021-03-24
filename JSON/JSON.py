#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  JSON.py
import json

#PROCESO JSON A PYTHON CODE
mijson='{ "name":"John", "age":30, "city":"New York"}'
#en python loads hace la funcion de parsear en otro lenguajes como java es parse(objetoJSON)
y=json.loads(mijson)
#acceder a su propiedad
print(y["age"])


#PROCESO INVERSO PYTHON CODE(diccionario) A JSON

#creamos un JSON
mijson={"name":"Jonathan",
		"edad":26}
#convierte el codigo python que es un dictionario y lo pasa JSON
y=json.dumps(mijson)
#imprime el JSON
print(y)
