archivo_nombre="python.txt"
with open(archivo_nombre,"r") as archivo:
    lineas_lista=archivo.readlines()
print(lineas_lista)

for linea in lineas_lista:
    print(linea)
    print()