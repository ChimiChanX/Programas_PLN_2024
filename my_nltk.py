import nltk
nltk.download("punkt")

archivo_nombre="nada.txt"

with open(archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

    
print("-----------------------------------------------------------------------------")
# Aquí, nuestra lista de tokens se llama "tokens"
palabras_total=len(tokens)
print(palabras_total)
print("-----------------------------------------------------------------------------")