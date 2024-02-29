print("universidad de colima")
print("ingenieria en computacion inteligente")
nombre=("Luis Fernando Figueroa Silva")
print("hola", nombre)
edad = input("escribe tu edad: ")
print(nombre, "tiene la edad de:", edad, "años")
print("opreacion: ", 4*5-6)
x=4+7
y=x-2
z=x+y
print("x= ", x)
print("y= ", y)
print("z= ", z)
 
#------------------------------------------------------------------------------------------

archivo_abierto=open("C:\\Users\\luisf\\OneDrive\\Documentos\\UdC\\6B\\OPTATIVA\\corazon.txt")
texto=archivo_abierto.read()
print(texto)
archivo_abierto.close()

#------------------------------------------------------------------------------------------

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