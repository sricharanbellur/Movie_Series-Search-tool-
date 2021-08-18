import csv
import time
def deleteprimary():
    tconst = input("""Enter the tconst of the movies you want to delete!!
    (Eg:tt0000000) : """)
    lines = list()
    start=time.time()
    with open('finalsmovies.csv', 'r',encoding='utf-8') as readFile:
        reader = csv.reader(readFile)
        found=False
        
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
    with open('finalmovies_deleted_primary.csv', 'w',newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
# deleteprimary()