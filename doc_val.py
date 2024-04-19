import nltk
from collections import Counter
import matplotlib.pyplot as plt
from docx import Document
import os

def leer_documento(nombre_archivo):
    try:
        doc = Document(nombre_archivo)
        texto = ""
        for para in doc.paragraphs:
            texto += para.text + "\n"
        return texto
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

# Variable para verificar si se ingresó correctamente el nombre del archivo
nombre_correcto = False

# Solicitar el nombre del archivo .docx al usuario
while True:
    nombre_archivo = input("Por favor, introduce el nombre del archivo .docx: ")

    if os.path.exists(nombre_archivo) and nombre_archivo.endswith('.docx'):
        nombre_correcto = True
        break
    else:
        print("El archivo ingresado no es válido o no existe. Inténtalo de nuevo.")

# Imprimir mensaje sobre la validez del nombre del archivo
if nombre_correcto:
    print("Se ingresó correctamente el nombre del documento.")
else:
    print("No se ingresó correctamente el nombre del documento. El programa se detendrá.")

texto = leer_documento(nombre_archivo)

if texto:
    # Guardar el texto extraído en un archivo de texto
    with open("texto_documento.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    # Contar el número de palabras
    num_palabras = len(texto.split())

    # Contar el número de líneas
    num_lineas = texto.count('\n') + 1

    print("Número de palabras en el documento:", num_palabras)
    print("Número de líneas de texto en el documento:", num_lineas)

    # Mostrar palabras de 3 o 4 caracteres
    palabras_3_4 = [palabra for palabra in texto.split() if 3 <= len(palabra) <= 4]
    print("Palabras de 3 o 4 caracteres:", palabras_3_4)

    # Contar el número de veces que aparece una palabra específica
    palabra_especifica = "específica"
    num_veces_palabra = texto.lower().count(palabra_especifica)
    print(f"La palabra '{palabra_especifica}' aparece {num_veces_palabra} veces en el texto.")

    print("----------------------------------------------------------------------")

    # Cargar palabras funcionales en español de NLTK
    nltk.download('stopwords')
    palabras_funcionales = set(nltk.corpus.stopwords.words("spanish"))

    print("----------------------------------------------------------------------")

    # Tokenizar el texto y eliminar palabras funcionales
    tokens = nltk.word_tokenize(texto, "spanish")
    tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

    # Imprimir algunos detalles sobre los tokens
    print(tokens_limpios)
    print("Número total de tokens:", len(tokens))
    print("Número de tokens limpios:", len(tokens_limpios))

    # Crear un objeto Text de NLTK y calcular la distribución de frecuencia
    texto_limpio_nltk = nltk.Text(tokens_limpios)
    distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

    # Graficar las 40 palabras más comunes
    distribucion_limpia.plot(40)
