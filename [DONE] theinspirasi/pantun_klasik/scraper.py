"""
17th June 2022 2:44pm (Malaysia time)
Irfan Zainudin

This scraper is provided for reference and educational purposes only.
It is not meant to be used for anyone except myself.
"""

import requests
from bs4 import BeautifulSoup

req = requests.get(
    "https://theinspirasi.my/pantun-melayu-yang-mempunyai-nilai-estetika-tinggi/"
)
doc = req.content
soup = BeautifulSoup(doc, "lxml")

for pantun_tag in soup.find_all("table"):
    with open("data.txt", "a") as output_file:
        output_file.write(pantun_tag.text)
        output_file.write("\n")
