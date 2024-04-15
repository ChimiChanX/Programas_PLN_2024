import os
archivo="fime.txt"

with open(archivo,"r") as archivo:
    texto=archivo.read()

simbolos=["(",")",",",",",";",":","\""]

for simbolo in simbolos:
    texto=texto.replace(simbolo," " + simbolo + " ")

palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
    print(palabra)