from selenium import webdriver
from bs4 import BeautifulSoup as bSoup
import pandas as pd
import requests
import array
URL = "https://www.vatanbilgisayar.com/samsung-apple/cep-telefonu-modelleri/?opf=p2000003%2Cp2500003%2F&min=4000&max=20000&srt=PU"

page = requests.get(URL)
soup = bSoup(page.content,"html.parser")
res_Title = []
res_Title = soup.findAll("div", class_ = "product-list__product-name")
res_Price = []
res_Price = soup.findAll("span", class_ = "product-list__price")
counter = 1
for title, price in zip(res_Title, res_Price):
    print("\nDevice #",counter,"\n----------------------------------------\n",title.text,"\n|",price.text,"|\n----------------------------------------")
    counter += 1