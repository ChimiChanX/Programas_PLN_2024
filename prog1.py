archivo_nombre = "nada.txt"
with open(archivo_nombre, "r") as archivo:
    lineas_lista = archivo.readlines()

num_linea = 1
lineas_con_texto = 0
lineas_vacias = 0

for linea in lineas_lista:
    if linea.strip() == "":
        print("Línea vacía", num_linea)
        lineas_vacias += 1
    else:
        print("Línea", num_linea, ":", linea.strip())
        lineas_con_texto += 1
    num_linea += 1

print("Total de líneas con texto:", lineas_con_texto)
print("Total de líneas vacías:", lineas_vacias)
print("Fin del Archivo")
