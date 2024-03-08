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
tokens_conjunto=set(tokens)

palabras_total=len(tokens)
palabras_diferentes=len(tokens_conjunto)

riqueza_lexica=palabras_diferentes/palabras_total

print("la riqueza lexica es: ", riqueza_lexica)
print("-----------------------------------------------------------------------------")

