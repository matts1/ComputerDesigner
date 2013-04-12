from bs4 import BeautifulSoup
import re

from general import *
from product import processProduct

def processCategory(url):
    page = getParsed('intel', url)
    table = page.find_all(class_='infoTable')[-1].find('tbody')
    products = {}
    for product in table.find_all('tr'):
        product = product.find_all('td')[1].find('a')
        productLink = product.attrs['href']
        productName = removeSymbols(product.contents[0].strip())
        print "Processing Product", productName
        products[(productLink, productName)] = processProduct(productLink)
    return products

if __name__ == "__main__":
    pprint(processCategory('/products/series/49428/Intel-Desktop-Boards-with-Intel-Atom-Processors'))
    pprint(processCategory('/products/family/65506/3rd-Generation-Intel-Core-i7-Processors/desktop'))
