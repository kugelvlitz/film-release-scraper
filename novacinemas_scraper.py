import requests
from bs4 import BeautifulSoup
import os

class NovacinemasScraper:
    def __init__(self):
        self.soup = BeautifulSoup(requests.get("https://www.novacinemas.cr/").content, "html.parser")

    def get_titles(self, release: str) -> list:

        # Depending on the value of release look for films now playing or upcoming releases
        release_class_label = ""
        if release == "upcoming":
            release_class_label = "upcoming"
        elif release == "current":
            release_class_label = "blockPremiere"
        else:
            print("Invalid type of release")
            return None

        films = self.soup.find_all("section", class_=release_class_label)[0]
        itemlist_div = films.find_all("div", class_="itemsList")[0]

        title_list = []
        for item in itemlist_div:
            title = item.find_all('h3')[0].text
            if title != "":
                title_list += [title]

        return title_list

    def get_latest_showing():
        pass

    def get_showing_times():
        pass

print(NovacinemasScraper().get_titles("upcoming"))