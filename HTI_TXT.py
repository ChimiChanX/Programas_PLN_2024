def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
        return None

def separar_y_ordenar_palabras(contenido):
    palabras = contenido.split()
    palabras_comillas = ' '.join([f'"{palabra}"' for palabra in palabras])
    palabras_ordenadas = sorted(palabras, reverse=True)
    
    return palabras_comillas, palabras_ordenadas

def main():

    nombre_archivo = "C:\\Users\\luisf\\OneDrive\\Documentos\\UdC\\6B\\OPTATIVA\\nada.txt"

    contenido = leer_archivo(nombre_archivo)

    if contenido:
        palabras_comillas, palabras_ordenadas = separar_y_ordenar_palabras(contenido)

        print("\nPalabras separadas por comillas:")
        print(palabras_comillas)

        print("\nPalabras ordenadas hacia abajo:")
        for palabra in palabras_ordenadas:
            print(palabra)

if __name__ == "__main__":
    main()
