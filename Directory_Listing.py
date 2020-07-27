import os
import re
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
directory=r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES"
content=os.listdir(r"/media/yousef/6a7721ee-4aef-4fec-8acf-614869125d1d/home/yousef/Desktop/SERIES")
with open(r"text.txt","w") as file:
    folders=[ name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) ]
    for x in folders:
        file.write(x+": " +"\n")
        for y in files(directory+ "/"+x):
            file.write("\t" + y +"\n")
