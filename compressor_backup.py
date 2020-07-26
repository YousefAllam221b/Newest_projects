import gzip
import shutil
with open('Documents\Python\messages-20200712', 'rb') as f_in:
    with gzip.open('Documents\out2', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
