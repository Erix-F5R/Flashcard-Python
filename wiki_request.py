import requests
import json
from bs4 import BeautifulSoup, NavigableString


def wiki_request(nom):

    return_list = []


    S = requests.Session()

    URL = "https://fr.wiktionary.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": nom,
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    htmlblock = BeautifulSoup(DATA["parse"]["text"]["*"], 'html.parser')


    #####FIND GENDER
    genderBlock = htmlblock.find_all('span', class_='ligne-de-forme' )
    return_list.append(genderBlock[0].contents[0].string)

    #####FIND TRANSLATIONS
    translationsBlock = htmlblock.find_all('div', class_='translations' )

    list_all_lang = translationsBlock[0].find_all('li')

    en_translations = ''


    for group in list_all_lang:
        #Select just the english translations
        if group.find(string='Anglais') != None:
            
            for child in group.descendants:
                if isinstance(child, NavigableString):
                    en_translations += child
                    
    return_list.append(en_translations.replace(u'\xa0', u' '))

    return return_list