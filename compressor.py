import time
import os

start = time.time()

os.system("tar -cvf name.tar Documents/Newest_projects")
os.system("gzip Documents/out.tar")

end = time.time()
print("Elapsed time: %s"%(end - start,))
