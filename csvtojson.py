import csv, json
import os
import pandas as pd


orders=pd.read_csv("movies2.csv")


data=orders.drop_duplicates(subset=['TITLE_ID','TITLE_NAME'])


df =pd.DataFrame(data[-13:])

df.values.tolist()



dfs = df.to_json(orient='records')
with open ("title.json","w") as jsonfile:
	json.dump(dfs,jsonfile,indent=4)

os.startfile("title.json")



