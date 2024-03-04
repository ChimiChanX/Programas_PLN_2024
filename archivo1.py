import my_nltk 

my_nltk.download('punkt')

#carpeta_nombre = "OPTATIVA\\"
archivo_nombre = "texto1.txt"


with open (archivo_nombre,"r") as archivo:
    texto=archivo.read()


tokens = my_nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)