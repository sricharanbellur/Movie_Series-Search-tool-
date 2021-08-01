import csv
import re
import time
import pandas as pd
from matplotlib import pyplot as plt
def secondarysearch_series():
        tvseries = input("""Enter the tv series to search : """)

        with open("finalseries.csv",errors='ignore') as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                count=0
                start=time.time()
                for line in reader:
                        
                        regex = re.compile(".*("+tvseries+").*",re.I)
                        try:
                                if regex.findall(line[1]):
                                        print("\nTconst :",line[0])
                                        print("\nTv series name :",line[1])
                                        print("\nStart Year :",line[2])
                                        print("\nEnd Year :",line[3])
                                        print("\nRun time :",line[4])
                                        print("\nGenre :",line[5])
                                        print("\nNumber of Votes :",line[6])
                                        print("\nRating :",line[7])
                                        found = True
                                        print("\n\\N indicates that the data has not been loaded\n")
                                        count+=1
                        except Exception:
                                pass
                print("Matches found :"+str(count))
                print('Do you want to save it in a csv file? [1/0]')
                save=int(input())
                if(save == 1 ):
                        with open("finalseries.csv") as file:
                                reader = csv.reader(file)
                        # skip the first row, since it is header.
                                header = next(reader)
                                tv_yearseries=open("tv_"+str(tvseries)+".csv","w",newline="")
                                writer=csv.writer(tv_yearseries)
                                writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                                for line in reader:
                                        try:
                                                if regex.findall(line[1]):
                                                        writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                        except Exception:
                                                pass
                                print('Check in the current directory for the csv file')
                else:
                        print('Ok')
                        
                        
                if not found:
                        print(tvseries, "not found")
                end=time.time()
                print('time taken to search the file in ms is:',round(end-start, 2))
                x = [0,10000,25000,50000,75000,100000,200000] 
                        # corresponding y axis values 
                y = [0,10000,25000,50000,75000,100000,200000]
                plt.plot(x, y) 

                
                                
                plt.xlabel('no of records') 
                plt.ylabel('time taken in msec') 
                        
                plt.title('search using primary key(tconst)') 
                
                                        # function to show the plot 
                plt.show() 