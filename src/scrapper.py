import requests
from bs4 import BeautifulSoup as bs

class Scrapper():

    def __init__(self):
        # stub constructor
        ...
    
    def get(self, currency):
        """
        get a search page html code, parse it and return article names
        """
        res = requests.get("https://www.google.com/search?q=site:coinmarketcap.com+" + currency)
        
        soup = bs(res.content, 'html.parser')
        articles = soup.find_all("h3")
        return articles


if __name__ == '__main__':
    scrapper = Scrapper()
    articles = scrapper.get("etherium")

    for article in articles:
        print(article.find("div").get_text())