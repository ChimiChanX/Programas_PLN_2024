import PyPDF2
import os
import re
from collections import Counter
import matplotlib.pyplot as plt

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def contar_lineas(texto):
    lineas = texto.split('\n')
    return len(lineas)

def contar_parrafos(texto):
    parrafos = re.split(r'\n\s*\n', texto)
    return len(parrafos)

def extraer_texto_pdf(pdf_path):
    with open(pdf_path, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        texto = ''
        for pagina in range(len(lector.pages)):
            texto += lector.pages[pagina].extract_text()
    return texto

def guardar_txt(texto, txt_path):
    with open(txt_path, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)

def graficar_frecuencia_palabras(texto):
    palabras = texto.split()
    contador = Counter(palabras)
    palabras_comunes = contador.most_common(20)
    
    palabras, frecuencias = zip(*palabras_comunes)
    
    plt.figure(figsize=(10, 6))
    plt.bar(palabras, frecuencias, color='blue')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.title('20 Palabras más comunes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Ruta del archivo PDF
    pdf_path = 'cuento3.pdf'
    
    # Extraer texto del PDF
    texto_extraido = extraer_texto_pdf(pdf_path)
    
    # Contar palabras, líneas y párrafos
    palabras = contar_palabras(texto_extraido)
    lineas = contar_lineas(texto_extraido)
    parrafos = contar_parrafos(texto_extraido)
    
    print(f'Palabras encontradas: {palabras}')
    print(f'Líneas encontradas: {lineas}')
    print(f'Párrafos encontrados: {parrafos}')
    
    # Guardar texto en un archivo .txt
    txt_path = 'documento.txt'
    guardar_txt(texto_extraido, txt_path)
    print(f'Texto guardado en {txt_path}')
    
    # Graficar frecuencia de palabras
    graficar_frecuencia_palabras(texto_extraido)
