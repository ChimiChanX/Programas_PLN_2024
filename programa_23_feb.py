import re


archivo_nombre = "Historia_Python.txt"

with open(archivo_nombre, "r") as archivo:
    texto = archivo.read()

expresion_regular=re.compile(r"(pero)?(hasta)? este?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))
    
    
expresion_regular=re.compile(r"\d+(,\d+)*(\.\d+)?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))