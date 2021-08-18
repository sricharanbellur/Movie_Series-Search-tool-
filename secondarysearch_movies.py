import csv
import re
import time
import pandas as pd
from matplotlib import pyplot as plt
from plotmovie_secondary import plotmovie_secondary
def secondarysearch_movie():
        movie = input("""Enter the movie to search : """)
        start=time.time()
        with open("finalsmovies.csv",encoding='utf-8',errors='ignore') as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                count=0
                
                for line in reader:
                        
                        regex = re.compile(".*("+movie+").*",re.I)
                        try:
                                if regex.findall(line[1]):
                                        print("\nTconst :",line[0])
                                        print("\nmovie name :",line[1])
                                        print("\nReleased Year :",line[2])
                                        print("\nGenre :",line[3])
                                        print("\nLanguage :",line[4])
                                        print("\nDirector : ",line[5])
                                        print("\nActors :",line[6])
                                        print("\nRating :",line[7])
                                        found = True
                                        print("\n\\N indicates that the data has not been loaded\n")
                                        count+=1
                        except Exception:
                                pass
                print("Matches found :"+str(count))
                end=time.time()
                print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
                print('Do you want to save it in a csv file? [1/0]')
                save=int(input())
                if(save == 1 ):
                        start=time.time()
                        with open("finalsmovies.csv",encoding="utf-8") as file:
                                reader = csv.reader(file)
                        # skip the first row, since it is header.
                                header = next(reader)
                                tv_yearseries=open("movie_"+str(movie)+".csv","w",newline="")
                                writer=csv.writer(tv_yearseries)
                                writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
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
                        print(movie, "not found")
                end=time.time()
                print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
                plotmovie_secondary()