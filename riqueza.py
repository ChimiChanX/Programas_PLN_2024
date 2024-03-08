import nltk

def riqueza_lexica(tokens):
    tokens_conjunto=set(tokens)
    palabras_totales=len(tokens)
    palabras_diferentes=len(tokens_conjunto)
    riqueza_lexica=palabras_diferentes/palabras_totales
    return riqueza_lexica

archivo_nombre="nada.txt"

with open(archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")
riqueza_lexica=riqueza_lexica(tokens)
print("-------------------------------------------------------------------")
print("La riqueza lexica es de", riqueza_lexica)
print("-------------------------------------------------------------------")