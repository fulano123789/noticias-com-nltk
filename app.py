from flask import Flask, render_template

import app_spacy
import app_nltk
import scraping

app = Flask(__name__)


'''
@app.route('/')
def index():
    return render_template('index.html')
'''


@app.route('/')
@app.route('/spacy')
@app.route('/spacy_newsapi')
def spacy_newsapi():
    noticias = scraping.obter_noticias_newsapi()  # Obtém notícias reais
    frases_coloridas = [app_spacy.colorir_palavras(noticia) for noticia in noticias]
    return render_template('index.html', frases=frases_coloridas)

@app.route('/spacy_globo')
def spacy_globo():
    noticias = scraping.obter_noticias_globo()  # Obtém notícias reais
    frases_coloridas = [app_spacy.colorir_palavras(noticia) for noticia in noticias]
    return render_template('index.html', frases=frases_coloridas)



@app.route('/nltk')
@app.route('/nltk_newsapi')
def nltk_newsapi():
    noticias = scraping.obter_noticias_newsapi()  # Obtém notícias reais
    frases_coloridas = [app_nltk.categorizar_palavras(noticia) for noticia in noticias]
    return render_template('index.html', frases=frases_coloridas)


@app.route('/nltk_globo')
def nltk_globo():
    noticias = scraping.obter_noticias_globo()  # Obtém notícias reais
    frases_coloridas = [app_nltk.categorizar_palavras(noticia) for noticia in noticias]
    return render_template('index.html', frases=frases_coloridas)




if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True)