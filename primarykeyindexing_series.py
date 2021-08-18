import csv 
import pyfiglet
from itertools import zip_longest
import pandas as pd
import time 
import sys
import matplotlib.pyplot as plt 
from plotseries_primary import plotseries_primary
def primarykey_series():
           ascii_banner = pyfiglet.figlet_format("PRIMARY KEY INDEXING ....") 
           print(ascii_banner) 
           Offset_address=[]
           Primary_key=[]
           csv_columns=["tconst", "Primary"]
           start=time.time()
           fi=open(r"finalseries.csv","r",encoding='utf-8')
           pos=fi.tell()
           line=fi.readline()
           while line:
               pos=fi.tell()
               line=fi.readline()
               a=line.split(",")
              #  print(pos,",",a[0])
               Offset_address.append(pos)
               Primary_key.append(a[0])

               
           list= [Offset_address, Primary_key]
           export_data = zip_longest(*list, fillvalue = '')
           with open('primaryKEY(series).csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(("Primary_Index", "tconst"))
                wr.writerows(export_data)
          
           print("Check the csv file primaryKEY(series).csv stored in your current working file directory")
           myfile.close()
           end=time.time()
           print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
           plotseries_primary()
#print('successful read')
           
#print('successful read')

# primarykey_series()