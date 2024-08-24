import requests
from bs4 import BeautifulSoup
import os

class CineMagalyScraper:
    def __init__(self):
        self.soup = BeautifulSoup(requests.get("https://cinemagaly.com/").content, "html.parser")

    def get_titles(self, release: str) -> list:
        films = self.soup.find_all('div', class_='ecommerce-card')

        titles = []
        for i in range(len(films)):
           titles += films[i].find_all('div', class_='item-name')[0].find_all('a')[0].contents

        return titles

    def get_latest_showing():
        pass

    def get_showing_times():
        pass

magaly = CineMagalyScraper()
print(magaly.get_titles("fasd"))