import requests
from bs4 import BeautifulSoup
import os


def get_titles(release: str) -> list:
    soup = BeautifulSoup(requests.get("https://www.novacinemas.cr/").content, "html.parser")

    release_class_label = ""
    if release == "upcoming":
        release_class_label = "upcoming"
    elif release == "current":
        release_class_label = "blockPremiere"
    else:
        print("Invalid type of release")
        return None

    film_divs = soup.find_all("section", class_=release_class_label)

    # La página contiene una única sección con la clase upcoming, donde están los próximos estrenos
    films = film_divs[0]

    # upcoming contienen una única item list
    itemlist_div = films.find_all("div", class_="itemsList")[0]

    title_list = []
    for item in itemlist_div:
        title = item.find_all('h3')[0].text
        if title != "":
            title_list += [title]

    return title_list

print(get_titles("current"))