import csv
import re
import time 
def deletesecondary():
    movies = input("""Enter the title of the movie you want to delete!!: """)
    lines = list()
   
    with open('finalsmovies.csv', 'r',encoding='utf-8') as readFile:
        reader = csv.reader(readFile)
        found=False
        count=0
        start=time.time()
        for row in reader:
            lines.append(row) 
            for field in row:
                regex = re.compile(".*("+movies+").*",re.I)
                if regex.findall(field):
                    print(row)
                    found=True
                    count+=1
        if found==False:
                    print('Not found')
        end=time.time()
        print("Found "+str(count)+" movies in","{0:.2f}".format(end-start)+" seconds" )
        tconst = input("""Enter the tconst of the above movie you want to delete!!
    (Eg:tt0000000) : """)
        lines = list()
        with open('finalsmovies.csv', 'r',encoding='utf-8') as readFile:
            reader = csv.reader(readFile)
            start=time.time()
            for row in reader:
                lines.append(row) 
                for field in row:
                    if field ==tconst:
                        lines.remove(row)
                        print(row,'deleted')
                        found=True
            if found==False:
                    print('Not found')
            end=time.time()
        print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
    with open('finalsmovies_deleted_secondary.csv', 'w',newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
# deletesecondary()