import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import json
import pdb
import types
import os

name=[]
def append_record(record):
    with open('Bibtex_format.json','a') as f:
         json.dump(record,f)
         f.write(os.linesep)

def store(data,file_name):
    with open(file_name, 'w') as json_file:
        json_file.write(json.dumps(data))


def get_json(file_name):
	jour=0
	conf=0
	list=[]
	diction={}
	number=[]
	name=[]
	bibdic={}
	f = open(file_name,'r')
	f1 = f.read()   #string
	f2 = f1.split("@")
	del f2[0]
	for a in f2:
		c=a.split(",\n") 
		del c[0]
		for mate in c:
			d=mate.split("=")
			if len(d)==2:   #type of d[0] is srtings
				bibdic[d[0]]=d[1]		
			if "title=" in mate:
				name.append(mate)
		append_record(bibdic)
	store(name,"title.json")
				
	

if __name__=="__main__":
	get_json("Bibtex.txt")
