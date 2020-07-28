import os
import re
import copy
directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"
adict={}
def extract_series():
	"""This function access the directory and creates a dict and a text.txt file which includes the directory tree."""
	with open("text.txt","w") as file:
		folders=os.listdir(directory)
		for folder in folders:
			p=os.listdir(directory+"/"+folder)
			adict[folder]={"files":[]}
			for i in p:
				if os.path.isdir(directory+"/"+folder+"/"+i):
					b=os.listdir(directory+"/"+folder+"/"+i)
					adict[folder][i]=b
				else:
					adict[folder]["files"]+=[i]

		for key in adict.keys():
			file.write(key+"\n")
			for a in adict[key]:
				file.write("\t"+a+"\n")
				for val in adict[key][a]:
					file.write("\t\t"+ val+"\n")
extract_series()
names=copy.deepcopy(adict)
def renaming():
	
	
	for key in names.keys():
		for a in names[key]:
			for val in names[key][a]:
				season=re.compile("(?=.*)(S\d\d|s\d\d)(?=.*)")
				episode=re.compile("(?=.*)(E\d\d|e\d\d)(?=.*)")
				se=season.findall(val)
				ep=episode.findall(val)
				if len(se) !=0 and len(ep) !=0: 
					names[key][a]= key +" "+ se[0] + " " + ep[0]

renaming()
print(names)



