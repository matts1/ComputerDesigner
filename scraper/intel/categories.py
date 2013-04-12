from bs4 import BeautifulSoup
import re

from general import *

def processProduct(url):
    return url

def processCategory(url):
    page = getParsed('intel', url)
    table = page.find_all(class_='infoTable')[1].find('tbody')
    products = {}
    for product in table.find_all('tr'):
        product = product.find_all('td')[1].find('a')
        productLink = product.attrs['href']
        productName = product.contents[0].strip()
        print removeSymbols(productName)
        products[productName] = processProduct(productLink)
    return products

processCategory('/products/family/65506/3rd-Generation-Intel-Core-i7-Processors/desktop')