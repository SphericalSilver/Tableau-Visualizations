# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:24:04 2019

@author: blueb
"""
import requests
import pandas as pd

dfs = pd.read_html("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters")
count = 0
for df in dfs:
    count += 1
    print(df.head())
    
clusters_info = dfs[1]
clusters_info.to_csv('clusters.csv')


dls = "https://www.moh.gov.sg/docs/librariesprovider5/diseases-updates/weekly-infectious-bulletin_caseswk32y2019.xlsx?sfvrsn=cceaba67_0"
resp = requests.get(dls)

output = open('denguetrends.xlsx', 'wb')
output.write(resp.content)
output.close()

trends = pd.read_excel('denguetrends.xlsx')
trends.to_csv('denguetrends.csv')