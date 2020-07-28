import os
import re

directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"


adict={}
with open("text.txt","w") as file:
	folders=os.listdir(directory)
	for folder in folders:
		p=os.listdir(directory+"/"+folder)
		adict[folder]=[]
		for i in p:

			if os.path.isdir(directory+"/"+folder+"/"+i):
				b=os.listdir(directory+"/"+folder+"/"+i)
				adict[folder]+=[{i:b}]



			else:
				adict[folder]+=p
for key in adict.keys():
	print(key)
	for a in adict[key]:
		if isinstance(a,list):
			print(a)
		elif isinstance(a,adict):
			for b in adict[key].keys():
				print(b)
				print(adict[key][b])

	# for folder in folders:
	# 	adict[folder]={}
	# 	if os.listdir(directory+"/"+folder) != []:
	# 		for subd in os.listdir(directory+"/"+folder):
	# 			adict[folder][subd]=[f for f in os.listdir(directory+"/"+folder) if os.path.isfile(os.path.join(directory+"/"+folder, f))]
	# 	else:
	# 		adict[folder]= [f for f in os.listdir(directory+"/"+folder) if os.path.isfile(os.path.join(directory+"/"+folder, f))]
	#
