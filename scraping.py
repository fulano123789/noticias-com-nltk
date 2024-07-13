import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


load_dotenv()


def obter_noticias_newsapi():

    try:
        # Obter o valor da variável NEWS_API_KEY
        NEWS_API_KEY = os.getenv('NEWS_API_KEY')

        url = f'https://newsapi.org/v2/top-headlines?country=br&apiKey={NEWS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        #noticias = [article['title'] for article in data['articles'] if article['title']]
        noticias = [f"{article['title']} ({article['title'].split(' - ')[1]})" for article in data['articles'] if ' - ' in article['title']]

        return noticias  
    except:
        erro = "Obtivemos um erro ao obter as noticias"
        noticias = []
        noticias.append(erro)
        return noticias  



def obter_noticias_globo():
    try:
        url = 'https://www.globo.com/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        noticias = []
        #<h2 class="post__title">Ministra: Abel 'errou, e muito' por expressão 'equipe de índios'</h2>
        for noticia in soup.find_all('h2', class_='post__title'):
            titulo = noticia.get_text().strip()
            if titulo:
                noticias.append(titulo+" (globo.com)")
    except:
        erro = "Obtivemos um erro ao obter as noticias"
        noticias = []
        noticias.append(erro)
        return noticias  
    return noticias

'''
index=0
noticias = obter_noticias_globo()
for noticia in noticias:
    index+=1
    print(index,")",noticia)
'''