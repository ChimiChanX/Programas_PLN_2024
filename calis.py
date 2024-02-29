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
    palabras_ordenadas = sorted(palabras)
    return palabras_ordenadas

def main():
    # Cambia la dirección del archivo según tu necesidad
    nombre_archivo = "C:\\Users\\luisf\\OneDrive\\Documentos\\UdC\\6B\\OPTATIVA\\nada.txt"

    contenido = leer_archivo(nombre_archivo)

    if contenido:
        palabras_ordenadas = separar_y_ordenar_palabras(contenido)

        print("\nPalabras ordenadas una por una en comillas:")
        for palabra in palabras_ordenadas:
            print(f'"{palabra}"')

if __name__ == "__main__":
    main()
