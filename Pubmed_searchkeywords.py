from Bio import Entrez
import types
import json
import pdb
from os import path


Entrez.email = 'huanghesong3231@yahoo.com'
list_json=[]
list_txt=[]

def get_json():
    with open('title.json') as json_file:
        data = json.load(json_file)   #list
        for m in data:
            m = m.replace("title={","")
            m = m.replace("}","")
            m = m.strip()
            list_json.append(m)
        print(list_json)
           

def search(query):
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='1',
                            retmode='xml',
                            term=query)
    results= Entrez.read(handle)
    list=results.get('IdList') 
    str = ''.join(list)
    return str
    
def getkeywords(id_number):
    file = open('keywords.txt', 'w')
    handle = Entrez.efetch(db="pubmed", id=id_number,rettype="abstract", retmode="xml")
    a=handle.read()
    b=a.split("\n")
    for c in b:
        if "Keyword MajorTopicYN" in c:  #string
           c = c.replace('<Keyword MajorTopicYN="N">',"")
           c = c.replace("</Keyword>","")
           list_txt.append(c)
    str_change = ''.join(list_txt)
    file.write(str_change)
    file.close()

if __name__=="__main__":
   get_json()
   for i in list_json:
       str = search(i)
       getkeywords(str)
