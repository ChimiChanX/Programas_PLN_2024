import requests
from bs4 import BeautifulSoup
import re

def contar_palabras_y_lineas(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
        texto_visible = soup.get_text()
        
        palabras = re.findall(r'\b\w+\b', texto_visible)
        num_palabras = len(palabras)
        
        lineas = texto_visible.split('\n')
        num_lineas = len(lineas)
        
        return num_palabras, num_lineas
    else:
        print("Error al obtener la página:", response.status_code)
        return None

url = 'https://acceso.mineduc.cl/wp-content/uploads/2021/06/Cuadernillo-Comprension-Lectora-adm2021.pdf'
resultado = contar_palabras_y_lineas(url)
if resultado:
    num_palabras, num_lineas = resultado
    print("Número de palabras en la página:", num_palabras)
    print("Número de líneas de texto en la página:", num_lineas)