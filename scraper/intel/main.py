from bs4 import BeautifulSoup
import re

from general import *
from categories import processCategory

def getLinks(table):
    links = table.find('tbody').find_all('a')
    return links

page = getParsed('intel', '/')

# also mobile products, software, embedded, but not including them
# sections is all the sections we want
sections = {
    ('DesktopProducts', 'Desktop') : ['Processors', 'Boards'],
    ('ServerProducts', 'Server') : ['Processors', 'Boards', 'Chassis', 'RAID'],
    ('SolidStateDrives', 'Storage') : ['SolidStateDrives', 'StorageProcessors'],
    ('NetworkingProducts', 'Networking') : ['Ethernet', 'Wireless'],
}

products = {}

for (section, name), parts in sections.items():
    products[name] = {}
    # eg. DesktopProducts-pane
    sectionId = section + '-pane'
    table = page.find('div', id=sectionId)
    for part in parts:
        products[name][splitCamelCase(part)] = {}
        idRegex = re.compile(r'%s-.*%s.*-scrollpane' % (section, part))
        for link in getLinks(table.find(id=idRegex)):
            products[name][splitCamelCase(part)][link.text] = processCategory(link.attrs['href'])