import os
import re

directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"


dict={}
with open("text.txt","w") as file:
	folders=os.listdir(directory)
	for folder in folders:
		p=os.listdir(directory+"/"+folder)
		dict[folder]=[]
		for i in p:
			
			if os.path.isdir(directory+"/"+folder+"/"+i):
				b=os.listdir(directory+"/"+folder+"/"+i)
				dict[folder]+=[{i:b}]
				
				
				
			else:
				dict[folder]+=p
for key in dict.keys():
	print(key)
	for a in dict[key]:
		if isinstance(a,list):
			print(a)
		elif isinstance(a,dict):
			for b in dict[key].keys():
				print(b)
				print(dict[key][b])

	# for folder in folders:
	# 	dict[folder]={}
	# 	if os.listdir(directory+"/"+folder) != []:
	# 		for subd in os.listdir(directory+"/"+folder):
	# 			dict[folder][subd]=[f for f in os.listdir(directory+"/"+folder) if os.path.isfile(os.path.join(directory+"/"+folder, f))]
	# 	else:
	# 		dict[folder]= [f for f in os.listdir(directory+"/"+folder) if os.path.isfile(os.path.join(directory+"/"+folder, f))]
	#
