import os
import re
import copy
directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop"
adict={}
def extract_series():
	"""This function access the directory and creates a dict and a text.txt file which includes the directory tree."""
	with open("text.txt","w") as file:
		folders=os.listdir(directory)
		adict={"folders":{},"files":[]}
		p=[]
		for folder in folders:
			
			if os.path.isdir(directory+"/"+folder):
				p=os.listdir(directory+"/"+folder)
				adict["folders"][folder]={}
				adict["folders"][folder]["files"]=[]
			

				for i in p:
					
					if os.path.isdir(directory+"/"+folder+"/"+i):
						
						b=os.listdir(directory+"/"+folder+"/"+i)
						adict["folders"][folder][i]=b
					else:
						adict["folders"][folder]["files"]+=[i]
			else:
				adict["files"]+=[folder]
		print(adict["folders"].keys())
		for key in adict.keys():
			file.write(key+"\n")
			if key !="files":
				for a in adict[key]:
					file.write("\t"+a+"\n")
					for val in adict[key][a]:
						file.write("\t\t"+ val+"\n")
						for aval in adict[key][a][val]:
							file.write("\t\t\t"+ aval+"\n")
			else:
				for a in adict[key]:
					file.write("\t"+a+"\n")
extract_series()
names=copy.deepcopy(adict)

