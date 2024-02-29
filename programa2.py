archivo_abierto=open("C:\\Users\\luisf\\OneDrive\\Documentos\\UdC\\6B\\OPTATIVA\\nada.txt","w")
archivo_abierto.write("esto se escribe en el archivo\n")
archivo_abierto.write("esto tambien\n")
archivo_abierto.write("mire, puedo escribir \"comillas\"\n")
archivo_abierto.write("gracias a las diagonales invertidas \n")
archivo_abierto.close

archivo_abierto=open("C:\\Users\\luisf\\OneDrive\\Documentos\\UdC\\6B\\OPTATIVA\\nada.txt")
texto=archivo_abierto.read()
print(texto)
archivo_abierto.close()