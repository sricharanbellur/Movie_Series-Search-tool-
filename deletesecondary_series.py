import csv
import re
import time 
def deletesecondaryseries():
    tvseries = input("""Enter the title of the tv series you want to delete!!: """)
    lines = list()
    with open('finalseries.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        found=False
        count=0
        start=time.time()
        for row in reader:
            lines.append(row) 
            for field in row:
                regex = re.compile(".*("+tvseries+").*",re.I)
                if regex.findall(field):
                    print(row)
                    found=True
                    count+=1
        if found==False:
                    print('Not found')
        end=time.time()
        print("Found "+str(count)+" movies in","{0:.2f}".format(end-start)+" seconds" )
        tconst = input("""Enter the tconst of the above tv series you want to delete!!
    (Eg:tt0000000) : """)
        lines = list()
        with open('finalseries.csv', 'r') as readFile:
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
    with open('finalseries_deleted_secondary.csv', 'w',newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)