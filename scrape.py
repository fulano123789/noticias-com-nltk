import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os




def obter_noticias():

    try:
        load_dotenv()

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


