import csv 
import pyfiglet
from itertools import zip_longest
import pandas as pd
import time 
import sys
import matplotlib.pyplot as plt 

def primarykey_series():
           ascii_banner = pyfiglet.figlet_format("PRIMARY KEY INDEXING ....") 
           print(ascii_banner) 
           Offset_address=[]
           Primary_key=[]
           csv_columns=["tconst", "Primary"]
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
           end=time.time()
           print('time taken to index using primary key the file in ms')
           print(round(end, 2))
            # x axis values 
           x = [10000,25000,50000,75000,100000,125000,150000,200000] 
           # corresponding y axis values 
           y = [10000,25000,50000,75000,100000,125000,150000,200000] 
           
             
            # plotting the points  
           plt.plot(x, y) 

  
           # naming the x axis 
           plt.xlabel('no of records') 
               # naming the y axis 
           plt.ylabel('time taken in msec') 
  
             # giving a title to my graph 
           plt.title('index using primary key') 
  
             # function to show the plot 
           plt.show() 
           
           myfile.close()
           
           
#print('successful read')

# primarykey_series()