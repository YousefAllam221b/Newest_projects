import pandas as pd
file_path = 'replaced'
pd.set_option("display.max_rows", None, "display.max_columns", None)
names=["Month" ,"Day" ,"Time" , "Machine", "State"]
df= pd.read_csv(file_path, sep=" " , usecols=range(5) ,names=names )
df3 = df.assign(Structure = df["Month"].astype(str) + ', ' + df["Day"].astype(str) + ', ' +df["Time"].astype(str) + ', ' +df["Machine"].astype(str) + ', ' +df["State"].astype(str))
print(df3)
