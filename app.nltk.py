from flask import Flask, render_template
from dotenv import load_dotenv
import os
import nltk
from nltk.tokenize import word_tokenize
from scrape import obter_noticias  # Importa a função de scraping

app = Flask(__name__)

# Carregar variáveis do arquivo .env
load_dotenv()

# Inicializar NLTK para o processamento em português
nltk.download('punkt')
nltk.download('floresta')

# Função para categorizar palavras usando NLTK
def categorizar_palavras(frase):
    tokens = word_tokenize(frase, language='portuguese')
    tags = nltk.pos_tag(tokens)  # 'eng' para usar o modelo de POS tagger do NLTK
    #tags = nltk.pos_tag(tokens, lang='portuguese')  # 'eng' para usar o modelo de POS tagger do NLTK

    # Mapeamento das tags para categorias gramaticais
    categorias_traduzidas = {
        'V': 'Verbo',
        'N': 'Substantivo',
        'ADJ': 'Adjetivo',
        'PRON': 'Pronome',
        'ADV': 'Advérbio',
        'ART': 'Artigo',
        'PREP': 'Preposição',
        'CONJ': 'Conjunção',
        'NUM': 'Numeral',
        'KC': 'Conjunção Coordenativa',
        'KS': 'Conjunção Subordinativa',
        'IN': 'Interjeição',
        'PCP': 'Particípio',
        'PDEN': 'Pronome Demonstrativo',
        'CUR': 'Pronome Indefinido',
        'PTKNEG': 'Negativa',
        'PRO-KS-REL': 'Pronome Relativo',
        'PROPESS': 'Pronome Pessoal',
        'PROSUB': 'Pronome Substantivo',
        'PU': 'Pontuação',
        'EC': 'Pronome Conexo',
        'ITJ': 'Interjeição',
        'ADVL': 'Adverbial',
        'FP': 'Forma Pronominal',
        'FORM': 'Forma Variável',
        'NPROP': 'Nome Próprio'
    }

    # Construção da frase categorizada
    frase_categorizada = []
    for token, tag in tags:
        categoria = categorias_traduzidas.get(tag, 'Desconhecido')
        palavra_categorizada = f'{token} ({categoria})'
        frase_categorizada.append(palavra_categorizada)

    return ' '.join(frase_categorizada)

@app.route('/')
def index():
    noticias = obter_noticias()  # Obtém notícias reais
    frases_categorizadas = [categorizar_palavras(noticia) for noticia in noticias]
    return render_template('index.html', frases=frases_categorizadas)

if __name__ == '__main__':
    app.run(debug=True)
