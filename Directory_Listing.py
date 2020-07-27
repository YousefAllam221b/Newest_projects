import os
import re

directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"


dict={}
with open("text.txt","w") as file:
	def list_files(startpath):
		for root, dirs, files in os.walk(startpath):
			level = root.replace(startpath, '').count(os.sep)
			indent = ' ' * 4 * (level)
			dict['{}{}'.format(indent, os.path.basename(root))]=[]
			file.write('{}{}:'.format(indent, os.path.basename(root))+"\n")
			subindent = ' ' * 4 * (level + 1)
			for f in files:
				dict['{}{}'.format(indent, os.path.basename(root))"]+=['{}{}'.format(subindent, f)+"\n"]
			    file.write('{}{}'.format(subindent, f)+"\n")
	list_files(directory)
for key in dict.keys():
	print(key)
	for value in dict.values():
		
		print(value)
