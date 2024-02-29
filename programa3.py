c = "C:\\Users\\luisf\\OneDrive\\Documentos\\UdC\\6B\\OPTATIVA\\"
e = "python.txt"
s = "archivo_nuevo.txt"

e2 = open(c + e, "r")
#print(e2.read())

s2=open(c+s,"w")
t=e2.read()
t2=t
s2.write(t2)

e2.close()
s2.close()

#s3=open(c+s, "r")
#print(s3.read())

with open (c+s, "r") as archivo:
    texto=archivo.read()
print(texto)

input("ingresa la palabra que deseas buscar: "  )
palabra=[]
if palabra in texto:
    print("\n \n encontre la palabra: ", palabra)
else:
    print("\n \n no encontre la palbra \n \n")


#s3.close()

