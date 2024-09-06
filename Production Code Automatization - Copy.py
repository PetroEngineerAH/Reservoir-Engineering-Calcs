# -*- coding: utf-8 -*-
"""
Created on Thu May 23 08:35:52 2024

@author: AHernandez
"""

import pandas as pd
import pyodbc 

import os
cnxn =  pyodbc.connect('Driver={SQL Server};'
        'Server=bogsql01\corex;'
        'Database=OFM_DB;'
        'Trusted_Connections=yes;')
          
script=""" SELECT*FROM DAILYPROD"""
df=pd.read_sql_query(script,cnxn)
df=df[['UNIQUEID','WELL_ID','DATE','HOURS','GAS','OIL','WATER']]
names = ['Akira', 'Tigana', 'Tigui', 'Tilo', 'Totoro', 'Bacano'] 
dfs = {}
df.to_excel("S:/Users/AHernandez/production_report1.xlsx")
folder = os.listdir("S:\Engineering\Res Engineering\Reservoir Production Surveillance\~Python Code")
data = pd.read_excel("S:/Engineering/Res Engineering/Reservoir Production Surveillance/~Python Code/Akira Noreste-1ST Production/AkiraNE1ST_Production_Updates.xlsm",sheet_name=None) 
# names = ['Akira', 'Tigana', 'Tigui', 'Tilo', 'Totoro', 'Bacano'] 
desired_files = []
prod_summary = data['Production Summary']
prod_summary_selected = prod_summary[['Unnamed: 0','Unnamed: 3','Unnamed: 4','Unnamed: 16']]
prod_summary_na = prod_summary_selected.fillna(0)
prod_summary['Unnamed: 10'] = prod_summary['Unnamed: 10'].astype('str')
prod_summary = prod_summary.drop([0,1,2,3,4])
print(prod_summary.dtypes)

