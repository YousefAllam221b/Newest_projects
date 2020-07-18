import pandas as pd
file_path = '/var/log/dmesg'
df= pd.read_csv(file_path)
df.head()
