# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:53:26 2024

@author: AHernandez
"""

import pypyodbc 
import pandas as pd 
import os 
import ctypes 
from pandas import ExcelWriter 
fpath = "S:\Engineering\Res Engineering\Reservoir Production Surveillance"
xlfile = "S:/Engineering/Res Engineering/Reservoir Production Surveillance/Akira Noreste-1ST Production/AkiraNE1ST_Production_Updates.xlsm"
cnxn = pypyodbc.connect('Driver={SQL Server};'
        'Server=bogsql01\corex;'
        'Database=Prod_Queries;'
        'Trusted_Connections=yes;')
         
script=""" SELECT*FROM 
Daily_Prod_DT_JO
"""
df=pd.read_sql_query(script,cnxn)

df=df[['BLOCK','FIELD','L_NAME','DATE','HOURS_OFF','OIL','WATER','gas','api','PIP_S','FORMACION','COMMENTARY']]
df.to_excel("FILEPATH") 
cursor = cnxn.cursor()

for subdir, dirs, files in os.walk(fpath):
    for file in files:
       #print(os.path.join(subdir,file))
        filepath = os.path.join(subdir,file)
        #print("FilePath: ", filepath)

        if filepath.endswith(".txt"):
            if file != "ClosedAging_Cont.txt":
                txtdata = open(filepath, 'r')
                script = txtdata.read().strip()
                txtdata.close()
                cursor.execute(script)
                if file == "ClosedAging.txt":
                    txtdata = open(os.path.join(subdir,"ClosedAging_Cont.txt"), 'r')
                    script = txtdata.read().strip()
                    txtdata.close()
                    cursor.execute(script)

                col = [desc[0] for desc in cursor.description]
                data = cursor.fetchall()
                df = pd.DataFrame(list(data),columns=col)

                #save_xls(df,xlfile)

                writer = pd.ExcelWriter(xlfile)
                flnm = file.replace('.txt','').strip()
                df.to_excel(writer,sheet_name=flnm,index=False)
                writer.save()

                print(file, " : Successfully Updated.")
            else:
                print(file, " : Ignoring this File")
        else:
            print(file, " : Ignoring this File") 