import pandas as pd
file_path = 'dmesg'
df= pd.read_csv(file_path, header=None, sep=" ", usecols=range(3))
df.head()
print(df)
