# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyodbc 
import pandas as pd 

cnxn =  pyodbc.connect('Driver={SQL Server};'
        'Server=bogsql01\corex;'
        'Database=OFM_DB;'
        'Trusted_Connections=yes;')
          
script=""" SELECT*FROM OFM_DB"""
df=pd.read_sql_query(script,cnxn)

df=df[['UNIQUEID','WELLID','DATE','HOURS','GAS','OIL','WATER']]
df.to_excel("S:/Users/AHernandez/production_report1.xlsx")

dfs = {}
for well in df['L_NAME'].unique().tolist():
    
    dfs[well] = df[df['L_NAME'] == well]
x = dfs['Tigana-08']

 
   