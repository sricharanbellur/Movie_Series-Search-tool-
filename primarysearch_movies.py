import csv
import time
from matplotlib import pyplot as plt
from plotmovie_primary import plotmovie_primary 
def primarysearch_movie():

    tconst = input("""Enter the tconst of the movie you want to search !!
    (Eg:tt0000000) : """)

    with open("finalsmovies.csv",encoding='utf8') as file:
        reader = csv.reader(file)
        # skip the first row, since it is header.
        header = next(reader)
        found = False
        start=time.time()
        for line in reader:
            
            if line[0] == tconst:
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
            
            
        if not found:
            print(tconst, "not found")
        end=time.time()
        print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
        plotmovie_primary()
    