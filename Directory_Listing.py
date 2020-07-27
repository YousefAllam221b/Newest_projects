import os
import re
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
directory=r"C:\Users\Yousef\Documents\Python\NEW_Projects"
content=os.listdir(r"C:\Users\Yousef\Documents\Python\NEW_Projects")
with open(r"C:\Users\Yousef\Documents\Python\NEW_Projects\text.txt","w") as file:
    folders=[ name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) ]
    for x in folders:
        file.write(x+": " +"\n")
        for y in files(directory+ "/"+x):
            file.write("\t" + y +"\n")
