import urllib2
from bs4 import BeautifulSoup

SITES = {
    'intel' : 'ark.intel.com',
}

SPECIAL_CHARACTERS = set([
    chr(174), #registered trademark (copyright with r)
    '\u2122', #tm
])

def getParsed(brand, url):
    url = url.split("://")
    if len(url) == 1:
        url = ["http", url[0]]
    url[1] = SITES[brand] + url[1]
    html = urllib2.urlopen("://".join(url)).read()
    return BeautifulSoup(html)

def splitCamelCase(text):
    text = list(text)
    text[0] = text[0].lower()
    output = [""]
    for letter in text:
        if letter.isupper():
            output.append(letter)
        else:
            output[-1] += letter
    output = [word.title() for word in output]
    return " ".join(output)

def removeSymbols(text):
    output = []
    for char in text:
        print char, repr(char), char in SPECIAL_CHARACTERS, SPECIAL_CHARACTERS
        if char not in SPECIAL_CHARACTERS:
            output.append(char)
    return ''.join(output)