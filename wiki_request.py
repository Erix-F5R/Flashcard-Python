import requests
import json
from bs4 import BeautifulSoup, NavigableString, ResultSet



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

    if 'error' in DATA:
        return_list.append('Genre Inconnu')
        return_list.append('Traductions pas trouvés')
        return return_list

    htmlblock = BeautifulSoup(DATA["parse"]["text"]["*"], 'html.parser')
    
    
  

    #####FIND GENDER
    genderBlock = htmlblock.find_all('span', class_='ligne-de-forme' )
    if len(genderBlock) > 0:
        return_list.append(genderBlock[0].contents[0].string)
    else:
        return_list.append('Genre inconnu')

    #####FIND TRANSLATIONS
    boites = htmlblock.find_all('div', class_='boite')    
    temp = ResultSet(None)
    
    for boite in boites:
         
        if boite.find(string='traductions à trier') != None:
            continue
                
        if boite.find('div', class_='translations') == None:
            continue        
        temp.append(boite.find('div', class_='translations'))            

    translationsBlock = temp

    en_translations = 'Anglais : '

    for list_all_lang in translationsBlock:


        list_all_lang = list_all_lang.find_all('li')
        for group in list_all_lang:
            #Select just the english translations
            if group.find(string='Anglais') != None :
                
                for child in group.descendants:
                    if isinstance(child, NavigableString):
                        if child != 'Anglais' and child != '\xa0: ':
                            en_translations += child
                en_translations += ' '

    return_list.append(en_translations.replace(u'\xa0', u' '))

    return return_list