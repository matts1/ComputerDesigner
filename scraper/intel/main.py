from bs4 import BeautifulSoup
import re

from general import *
from categories import processCategory

def Intel():
    sections = {
        ('DesktopProducts', 'Desktop') : ['Processors', 'Boards'],
        ('ServerProducts', 'Server') : ['Processors', 'Boards', 'Chassis', 'RAID'],
        ('SolidStateDrives', 'Storage') : ['SolidStateDrives', 'StorageProcessors'],
        ('NetworkingProducts', 'Networking') : ['Ethernet', 'Wireless'],
    }
    cacheIntel(sections)

def cacheIntel(sections):
    page = getParsed('intel', '/')

    # also mobile products, software, embedded, but not including them
    # sections is all the sections we want


    products = {}

    for (section, name), parts in sections.items():
        products[name] = {}
        # eg. DesktopProducts-pane
        sectionId = section + '-pane'
        table = page.find('div', id=sectionId)
        for part in parts:
            print "Processing hardware type", name
            products[name][splitCamelCase(part)] = {}
            idRegex = re.compile(r'%s-.*%s.*-scrollpane' % (section, part))
            for link in getLinks(table.find(id=idRegex)):
                category = removeSymbols(link.text)
                print "Processing category", category
                products[name][splitCamelCase(part)][category] = processCategory(link.attrs['href'])

def getLinks(table):
    links = table.find('tbody').find_all('a')
    return links

if __name__ == "__main__":
    Intel()
