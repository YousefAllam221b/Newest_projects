import os
import re
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"
content=os.listdir(r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES")
def getfolders(directory):
    folders=[ name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) ]
    return folders
def getfiles(d):
    out=[]
    for y in files(directory+ "/"+d):
          out+=[y]
    return out

with open(r"text.txt","w") as file:
	for x in getfolders(directory):
		print(x)
		file.write(x+": \n")
		print(getfiles(x))
		for y in getfiles(x):
			file.write(y+"\n")
