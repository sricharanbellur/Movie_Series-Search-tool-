import csv
import time
from matplotlib import pyplot as plt
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