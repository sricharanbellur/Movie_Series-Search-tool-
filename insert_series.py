import csv
def insert_series():
    tconst1 = input("""Enter the tconst of the tv series you want to insert !!
    (Eg:tt0000000) : """)
    with open(r"finalseries.csv", "r",encoding='utf-8',newline="") as csvfile:
                        if tconst1 in csvfile.read():
                            print("tconst already exists")
                        else:
                            print("Enter \\N for empty entry")
                            tconst = input('Enter the tconst:')
                            primarytitle= input('enter the title :')
                            startYear= input('enter the start year :')
                            endYear = input('enter the end year:')
                            runtimeMinutes = input('enter the runtime:')
                            genres = input('enter the genre:')
                            numVotes=input('enter the number of votes:')
                            averageRating=input('enter the average rating:')
                            with open('finalseries.csv','a+',newline="") as csvfile:
                            #    readCSV = csv.reader(csvfile, delimiter=',')
                                filedname = [tconst,primarytitle,startYear,endYear,runtimeMinutes,genres,numVotes,averageRating]
                                print(filedname)
                                writer = csv.writer(csvfile,lineterminator='\n')
                                writer.writerow(filedname)