c = "C:\\Users\\luisf\\OneDrive\\Documentos\\UdC\\6B\\OPTATIVA\\"
e = "python.txt"
s = "archivo_nuevo.txt"

with open(c + e, "r") as e2:
    t = e2.read()

with open(c + s, "w") as s2:
    s2.write(t)

with open(c + s, "r") as archivo:
    texto = archivo.read()
    print(texto)

palabra = input("Ingresa la palabra que deseas buscar: ")

if palabra in texto:
    print("\nEncontré la palabra:", palabra)
else:
    print("\nNo encontré la palabra.\n")
