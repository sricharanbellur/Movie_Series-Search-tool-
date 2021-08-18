import csv
import time 
import pyfiglet
from itertools import zip_longest
import pandas as pd
from plotmovie_primary import plotmovie_primary 
import matplotlib.pyplot as plt 

def primarykey_movie():
           ascii_banner = pyfiglet.figlet_format("PRIMARY KEY INDEXING ....") 
           print(ascii_banner) 
           Offset_address=[]
           Primary_key=[]
           csv_columns=["tconst", "Primary"]
           start=time.time()
           fi=open(r"finalsmovies.csv","r",encoding='utf-8')
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
           with open('primaryKEY_movies.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(("Primary_Index", "tconst"))
                wr.writerows(export_data)
           myfile.close()
           print("Check the csv file primaryKEY_movies.csv stored in your current working file directory")
           end=time.time()
           print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
           plotmovie_primary()
#print('successful read')

# primarykey_movie()