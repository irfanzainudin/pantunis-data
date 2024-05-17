"""
17th June 2022 2:44pm (Malaysia time)
Irfan Zainudin

This scraper is provided for reference and educational purposes only.
It is not meant to be used for anyone except myself.
"""

import requests
from bs4 import BeautifulSoup


for i in range(1, 2):
    req = requests.get(
        f"http://www.malaycivilization.com.my/items/browse?collection=10&page={str(i)}&output=rss2"
    )
    doc = req.content
    soup = BeautifulSoup(doc, "lxml")
    print(soup)
    # for pantun_tag in soup.find_all("table"):
    #     print(pantun_tag)
    # with open("data.txt", "a") as output_file:
    #     output_file.write(pantun_tag.text)
    #     output_file.write("\n")
    break
