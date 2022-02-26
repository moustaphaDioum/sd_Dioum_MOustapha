#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:45:12 2022

@author: moustaphe
"""

from json import dump as jdump
from json import load
from json import loads
from json import dumps
from yaml import dump as ydump
from yaml import safe_load
from csv import DictReader as csv_load
from csv import DictWriter as csv_write
from xmltodict import parse
from dicttoxml import dicttoxml as dtx


# fonction permettant de lire un fichier avec une extension donnée et de le mettre sous format dico en python

def convert_to_dict(file):
    reader = ''
    with open(file, 'r') as thefile:
        if file.endswith('.json'):
            reader = load(thefile)
        elif file.endswith('.yaml') or file.endswith('.yml'):
            reader = safe_load(thefile)
        elif file.endswith('.csv'):
            # this = {}
            list = []
            #k = 0
            reader = csv_load(thefile)
            # for element in reader:
            #     list.setdefault("value" + str(k), element)
            #     k +=1
            # reader = list
            for element in reader:
                list.append(element)
            reader = list
        elif file.endswith('.xml'):
            reader = loads(dumps(parse(thefile.read())))
        return reader

#print(convert_to_dict('dioum.json'))
#print(convert_to_dict('dioum.xml'))
#print(convert_to_dict('notes.csv'))
# fonction permettant de convertir un dico en un format fichier de donnée en parametre

def converter(pdata, name, extent):
    with open(f'{name}.{extent}', 'w') as target:
        if extent == 'json':
            jdump(dumps(pdata), target)
        elif extent == 'yaml' or extent == 'yml':
            ydump(pdata, target)
        elif extent == 'csv':
            pdata = [pdata]
            fieldnames = pdata[0].keys()
            # n = int(input("Entrer la taille de l'entete: "))
            # fieldnames = [input() for i in range(n)]
            output = csv_write(target, fieldnames)
            output.writeheader()
            for elem in pdata:
                output.writerow(elem)
        elif extent == 'xml':
            xml = dtx(pdata)
            target.write(str(xml, 'utf-8'))
        else:
            print("Ce format de fichier n'est pas pris en compte !")

    print(f"{name}.{extent} est créé avec succès ! " )
