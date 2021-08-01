import csv 
import pyfiglet
from itertools import zip_longest
import pandas as pd
import time 
import sys
import matplotlib.pyplot as plt 
def secondarykey_series():
            ascii_banner = pyfiglet.figlet_format("Secondary KEY INDEXING ....") 
            print(ascii_banner) 
            Offset_address=[]
            Secondary_key=[]
            csv_columns=["primarytitle", "Secondary_Key"]
            fi=open(r"finalseries.csv","r",encoding='utf-8',newline="")
            tvseries=open("secondaryKey_series.csv","w",encoding="utf-8",newline='')
            writer=csv.writer(tvseries)
            writer.writerow(["Secondary_Index","primarytitle"])
            pos=fi.tell()
            line=fi.readline()
            try:
                while line:
                    a=line.split(",")
                    pos=fi.tell()
                    line=fi.readline()
                    a=line.split(",")
                    Offset_address.append(pos)
                    Secondary_key.append(a[1])
                    writer.writerow([pos,a[1]])
            #    print(pos,a[1])
            except:
                print()
            print('Check in the current directory for the csv file')
            # tvseries=open("secondarykey.csv","w",newline="")
            # writer=csv.writer(tvseries)
            # writer.writerow(["primarytitle","secondary"])
            # for line in list:
            #         writer.writerow([a[1],pos])
            

secondarykey_series()
