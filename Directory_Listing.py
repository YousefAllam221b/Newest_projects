import os
import re

directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"


dict={}
with open("text.txt","w") as file:
	folders=os.listdir(directory)
	for folder in folders:
		dict[folder]={}
		if os.listdir(directory+"/"+folder) != []:
			for subd in os.listdir(directory+"/"+folder):
				dict[folder][subd]=[f for f in os.listdir(directory+"/"+folder) if os.path.isfile(os.path.join(directory+"/"+folder, f))]
		else:
			dict[folder]= [f for f in os.listdir(directory+"/"+folder) if os.path.isfile(os.path.join(directory+"/"+folder, f))]
	for key in dict.keys():
		print(key)
		file.write(key +": \n")
		if type(dict[key]) == 'list':
			print(dict[key])
			file.write(dict[key] +" \n")
		else:
			for akey in dict[key].keys():
				file.write(akey +": \n")
				if type(dict[key][akey]) == 'list':
					print(dict[key][akey])
					file.write(dict[key][akey] +" \n")










