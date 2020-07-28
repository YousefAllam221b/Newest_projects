import os
import re

directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"


adict={}
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

		

	# for folder in folders:
	# 	adict[folder]={}
	# 	if os.listdir(directory+"/"+folder) != []:
	# 		for subd in os.listdir(directory+"/"+folder):
	# 			adict[folder][subd]=[f for f in os.listdir(directory+"/"+folder) if os.path.isfile(os.path.join(directory+"/"+folder, f))]
	# 	else:
	# 		adict[folder]= [f for f in os.listdir(directory+"/"+folder) if os.path.isfile(os.path.join(directory+"/"+folder, f))]
	#
