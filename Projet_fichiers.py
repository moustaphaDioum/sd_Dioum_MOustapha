#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:43:18 2022

@author: moustaphe
"""

from os import listdir
from os import getcwd
from os import chdir
from os.path import isfile
from os.path import abspath
from fonction_conv import convert_to_dict
from fonction_conv import converter


current_folder = getcwd() #savoir dans kel dossier nous sommes
foldername = input("Vous etes dans le dossier "+ current_folder + "\nEntrer le chemin du dossier ou on doit chercher les fichiers: ")
try:
    chdir(foldername) #chdir permet de changer le repertoire de travail
except FileNotFoundError:
    print("Ce dossier n'existe pas !")

extents = ['json', 'xml', 'yaml', 'yml', 'csv']
myfiles = []
for file in listdir('.'): #listdir sort tous les fichiers dans le dossier
    extension = file.split('.')[-1] #on recupere l'extension
    if extension in ['json', 'xml', 'yaml', 'yml', 'csv']:
        if isfile(abspath(file)):   #abspath() renvoi le chemin du fichier donne et isfile verifie si le chemin est bon
            myfiles.append(file) #on stock l'ensemble de nos fichiers dans cette liste

print(50*'*')
print("Choisir un fichier: ")
for i in range(len(myfiles)):
    print(i + 1, '-', myfiles[i])

choice = int(input("choissisez votre fichier: "))

choice_name = myfiles[choice - 1].split('.')[0]  #on recupere le nom du fichier choisi
choice_extent = myfiles[choice - 1].split('.')[-1] #on recupere ici l'extension du fichier choisi
print("vous avez choisi", myfiles[choice - 1])


if choice_extent in ['yaml', 'yml']:
    extents.remove('yaml')
    extents.remove('yml')
else:
    extents.remove(choice_extent)

print("Choisissez un format de sortie: ")
for format in extents:
    print(format, " ", end="")
print()

output_extent =''
while output_extent not in extents:
    print("Choisir le bon format de fichier: ")
    output_extent = input()

pdata = convert_to_dict(myfiles[choice - 1])
converter(pdata, choice_name, output_extent)
# print(myfiles)
# print(extents)