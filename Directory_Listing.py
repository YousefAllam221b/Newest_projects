import os
import re

directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"


dict={}
with open("text.txt","w") as file:
	folders=os.listdir(directory)
	for folder in folders:
		dict[folder]=[]
		if os.listdir(directory+"/"+folder) != []:
			for subd in folder:
				dict[folder][subd]=[f for f in listdir(directory+"/"+folder) if isfile(join(directory+"/"+folder, f))]
		else:
			dict[folder]= [f for f in listdir(directory+"/"+folder) if isfile(join(directory+"/"+folder, f))]
print(dict)
