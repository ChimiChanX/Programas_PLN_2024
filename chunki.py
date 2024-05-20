import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser

# Descargar los recursos necesarios
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Definir una función para aplicar chunking a un texto
def chunk_text(text):
    # Tokenizar el texto en palabras
    words = word_tokenize(text)
    
    # Etiquetar las palabras con POS tags
    tagged_words = pos_tag(words)
    
    # Definir la gramática para chunking
    grammar = """
      NP: {<DT>?<JJ>*<NN>}   # Frase nominal
      VP: {<VB.*><NP|PP|CLAUSE>+$}  # Frase verbal
      PP: {<IN><NP>}         # Frase preposicional
      CLAUSE: {<NP><VP>}     # Clausula
    """
    
    # Crear el parser con la gramática definida
    chunk_parser = RegexpParser(grammar)
    
    # Aplicar el parser a las etiquetas POS
    chunked = chunk_parser.parse(tagged_words)
    
    return chunked

# Texto de ejemplo
text = "The quick brown fox jumps over the lazy dog."

# Aplicar chunking al texto
chunked_text = chunk_text(text)

# Mostrar el resultado
print(chunked_text)

# Dibujar el árbol de chunking
chunked_text.draw()
