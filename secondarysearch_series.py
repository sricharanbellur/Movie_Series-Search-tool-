import csv
import re
import time
import pandas as pd
from matplotlib import pyplot as plt
from plotseries_secondary import plotseries_secondary
def secondarysearch_series():
        tvseries = input("""Enter the tv series to search : """)
        start = time.time()
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
                end=time.time()
                print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
                save=int(input())
                if(save == 1 ):
                        start=time.time()
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
                                end=time.time()
                                print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
                                plotseries_secondary()
                else:
                        print('Ok')
                        
                        
                if not found:
                        print(tvseries, "not found")
      