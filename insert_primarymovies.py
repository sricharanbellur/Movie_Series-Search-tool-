import csv
def insert_movie():
    tconst1 = input("""Enter the tconst of the movie you want to insert !!
    (Eg:tt0000000) : """)
    with open(r"finalsmovies.csv", "r",encoding='utf-8',newline="") as csvfile:
                        if tconst1 in csvfile.read():
                            print("tconst already exists")
                        else:
                            print("Enter \\N for empty entry")
                            tconst = input('Enter the tconst: ')
                            primarytitle= input('enter the title : ')
                            year= input('Enter the year of release :')
                            genres = input('enter the genre: ')
                            language = input('Enter the language: ')
                            director=input('Enter the director: ')
                            actors=input("Enter the actors Give ',' between the actors to insert: ")
                            averageRating=input('enter the average rating: ')
                            with open('finalsmovies.csv','a+',newline="") as csvfile:
                            #    readCSV = csv.reader(csvfile, delimiter=',')
                                filedname = [tconst,primarytitle,year,genres,language,director,actors,averageRating]
                                print(filedname)
                                writer = csv.writer(csvfile,lineterminator='\n')
                                writer.writerow(filedname)