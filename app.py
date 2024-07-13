from flask import Flask, render_template
import requests
import spacy
from scrape import obter_noticias  # Importa a função de scraping

app = Flask(__name__)

# Carregar o modelo de SpaCy para português
nlp = spacy.load("pt_core_news_sm")

# Função para colorir palavras de acordo com a classe gramatical
def colorir_palavras(frase):
    doc = nlp(frase)

    cores = {
        'VERB': 'red',        # Verbo
        'NOUN': 'blue',       # Substantivo
        'ADJ': 'green',       # Adjetivo
        'PRON': 'orange',     # Pronome
        'ADV': 'purple',      # Advérbio
        'DET': 'cyan',        # Determinante
        'ADP': 'brown',       # Preposição
        'AUX': 'pink',        # Auxiliar
        'CONJ': 'grey',       # Conjunção
        'INTJ': 'yellow',     # Interjeição
        'NUM': 'magenta',     # Numeral
        'PART': 'lime',       # Partícula
        'SCONJ': 'olive',     # Conjunção subordinativa
        'SYM': 'black',       # Símbolo
        'X': 'maroon'         # Outros
    }

    # Tradução das categorias gramaticais
    categorias_traduzidas = {
        'VERB': 'Verbo',
        'NOUN': 'Substantivo',
        'ADJ': 'Adjetivo',
        'PRON': 'Pronome',
        'ADV': 'Advérbio',
        'DET': 'Determinante',
        'ADP': 'Preposição',
        'AUX': 'Verbo Auxiliar',
        'CONJ': 'Conjunção',
        'INTJ': 'Interjeição',
        'NUM': 'Numeral',
        'PART': 'Partícula',
        'SCONJ': 'Conjunção Subordinativa',
        'SYM': 'Símbolo',
        'X': 'Outros'
    }

    frase_colorida = []
    for token in doc:
        cor = cores.get(token.pos_, 'black')
        categoria = categorias_traduzidas.get(token.pos_, 'Desconhecido')
        palavra_colorida = f'<span style="color: {cor};" title="{categoria}">{token.text}</span>'
        frase_colorida.append(palavra_colorida)

    return ' '.join(frase_colorida)

@app.route('/')
def index():
    noticias = obter_noticias()  # Obtém notícias reais
    frases_coloridas = [colorir_palavras(noticia) for noticia in noticias]
    return render_template('index.html', frases=frases_coloridas)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)