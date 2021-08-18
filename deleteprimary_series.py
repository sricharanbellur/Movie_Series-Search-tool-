import csv
import time 
def deleteprimaryseries():
    tconst = input("""Enter the tconst of the tv series you want to delete!!
    (Eg:tt0000000) : """)
    lines = list()
    with open('finalseries.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        found=False
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
    with open('finalseries_deleted_primary.csv', 'w',newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
# deleteprimaryseries()