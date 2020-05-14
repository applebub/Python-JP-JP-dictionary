# -*- coding: utf-8 -*-


import csv
import requests


def textformat(s):                                                             #function which corrects text given by API
    
    part=[]                                                                    #will keep list of parts from text  to be deleted

    characters = "qwertyuiopasdfghjklzxcvbnm\\/1234567890"
    
    for i in range(len(s)):
        if s[i] == "[" and s[i+1] in characters:
            j = s[i:].find("]")
            if s[i:i+j+1] not in part:
                part.append(s[i:i+j+1])
            i=j
    
    s1 = part.copy()
    s1[0] = s
    s1.append("")
    count = 1
    
    for z in part:
        s1[count] = s1[count-1].replace(z, "")
        count+=1
    
    return s1[-1]

def dic(word):                                                                 #Shows japanese definition of given word
        
    response = requests.get("https://sakura-paris.org/dict/?api=1", params={"q":word, "dict":"広辞苑", "max":"1"})
    text = response.json()
    st = text['words'][0]['text']    
 
    return textformat(st).replace("\n", "")


def create():                                                                  #Creates list from txt file  named files.txt where are stored words 
    peace = []
    test = open("file.txt","r", encoding="utf-8")
    peace = test.read().split()
    return peace
 

lista = create()
definition = lista.copy()
index = 0

for w in lista:                                                                #For every word it finds a definiton
    print(w)                                                                   #Print is here in case of error to show which word caused it.
    definition[index] = dic(w)
    index+=1


with open("test.csv", "w", newline="", encoding="utf-8") as slownik:           #Creates new csv file(test.csv) with list of words and in next column list of japanese definitions corresponding to them. 
    automat = csv.writer(slownik, delimiter=";", quotechar=";" )
    for h in range(len(lista)):
        automat.writerow([lista[h], definition[h]])
        
