import csv
import time
import re
import pandas as pd
def selectivesearch_movie():
    while True:
        print("\nPRESS 1 to search a particular movie by its title")
        print("PRESS 2 to obtain the movie according to  year")
        print("PRESS 3 to obtain all the movies by a particular director")
        print("PRESS 4 to obtain all the movies by a particular actor")
        print("PRESS 5 to obtain all the movies by a particular language")
        print("PRESS 6 to obtain all the movies by a particular genre")
        print("PRESS 7 to obtain by rating:\n")
        print("PRESS 0 to Exit")
        choice=int(input())
        if(choice==1):
            
            movie= str(input("Enter the name of movie you want to find :"))
            start = time.time()
            with open("finalsmovies.csv",encoding="utf-8") as file:
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
                            print("\nDirector :",line[5])
                            print("\nActors :",line[6])
                            print("\nRating :",line[7])
                            found = True
                            print("\n\\N indicates that the data has not been loaded\n")
                            count+=1
                    except Exception:
                        pass
                        
                if not found:
                    print(movie, " is not found")

            print("Matches found :"+str(count))
            end=time.time()
            print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
        elif(choice == 2):
            while True:
                print("\nPRESS 1 to obtain all movie according to one particular start year")
                print("PRESS 2 to obtain the movie by its title and its start year")
                print("PRESS 3 to obtain all the movie present between two years of your choice")
                print("PRESS 4 to obtain all the movie started after a  particular year")
                print("PRESS 5 to obtain all the movie started before a  particular year\n")
                print("PRESS 0 to Exit")
                choiceyear=int(input())
                if(choiceyear==1):
                    
                    tvyear=str(input("Enter the start year  :"))
                    with open("finalsmovies.csv",encoding='utf-8') as file:
                        reader = csv.reader(file)
                        # skip the first row, since it is header.
                        header = next(reader)
                        found = False
                        count = 0
                        for line in reader:
                            try:
                                if line[2] ==tvyear :
                                    print("\nTconst :",line[0])
                                    print("\nmovie name :",line[1])
                                    print("\nReleased Year :",line[2])
                                    print("\nGenre :",line[3])
                                    print("\nLanguage :",line[4])
                                    print("\nDirector :",line[5])
                                    print("\nActors :",line[6])
                                    print("\nRating :",line[7])
                                    found = True
                                    print("\n\\N indicates that the data has not been loaded\n")
                                    count+=1
                            except Exception:
                                pass
                        print("Matches found :"+str(count))
                        print('Do you want to save it in a csv file? [1/0]')
                        save=int(input())
                        if(save == 1 ):
                            with open("finalsmovies.csv",encoding='utf-8') as file:
                                reader = csv.reader(file)
                        # skip the first row, since it is header.
                                header = next(reader)
                                tv_yearmovie=open("tvyear_"+str(tvyear)+".csv","w",newline="")
                                writer=csv.writer(tv_yearmovie)
                                writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"]
            )
                                for line in reader:
                                    try:
                                        if line[2]==tvyear:
                                            writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                    except Exception:
                                        pass
                                print('Check in the current directory for the csv file')
                        else:
                            print('Ok')
                        if not found:
                            print("not found")
                elif(choiceyear==2):
                    
                    movie = str(input("Enter the name of movie you want to find :"))
                    tvyear=str(input("Enter the start year of that movie :"))
                    with open("finalsmovies.csv",encoding='utf-8') as file:
                        reader = csv.reader(file)
                        # skip the first row, since it is header.
                        header = next(reader)
                        found = False
                        for line in reader:
                            regex = re.compile(".*("+movie+").*",re.I)
                            try:
                                if line[2] == tvyear and regex.findall(line[1]):
                                    print("\nTconst :",line[0])
                                    print("\nmovie name :",line[1])
                                    print("\nReleased Year :",line[2])
                                    print("\nGenre :",line[3])
                                    print("\nLanguage :",line[4])
                                    print("\nDirector :",line[5])
                                    found = True
                                    print("\n\\N indicates that the data has not been loaded\n")
                            except Exception:
                                pass
                                
                        if not found:
                            print("not found")
                            
                elif(choiceyear==3):
                    tvyear1=int(input("Enter the from year to start with:"))
                    tvyear2=int(input("Enter the to year :"))
                
                    with open("finalsmovies.csv",encoding='utf-8') as file:
                            reader = csv.reader(file)
                            # skip the first row, since it is header.
                            header = next(reader)
                            found = False
                            count = 0
                            for line in reader:
                                try:
                                    if int(line[2]) >=tvyear1 and int(line[2]) <= tvyear2 :
                                        print("\nTconst :",line[0])
                                        print("\nmovie name :",line[1])
                                        print("\nReleased Year :",line[2])
                                        print("\nGenre :",line[3])
                                        print("\nLanguage :",line[4])
                                        print("\nDirector :",line[5])
                                        print("\nActors :",line[6])
                                        print("\nRating :",line[7])
                                        found = True
                                        print("\n\\N indicates that the data has not been loaded\n")
                                        count+=1
                                except Exception:
                                    pass
                            print("Matches found :"+str(count))
                            print('Do you want to save it in a csv file? [1/0]')
                            save=int(input())
                            if(save == 1 ):
                                with open("finalsmovies.csv",encoding='utf-8') as file:
                                    reader = csv.reader(file)
                            # skip the first row, since it is header.
                                    header = next(reader)
                                    tv_yearmovie=open("tvyear_"+str(tvyear1)+" to "+str(tvyear2)+".csv","w",newline="")
                                    writer=csv.writer(tv_yearmovie)
                                    writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"]
            )
                                    for line in reader:
                                        try:
                                            if int(line[2]) >=tvyear1 and int(line[2]) <= tvyear2 :
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                        except Exception:
                                            pass
                                    print('Check in the current directory for the csv file')
                            else:
                                    print('Ok')
                            if not found:
                                print("not found")
                                
                elif(choiceyear==4):
                    tvyear1=int(input("Enter the year:"))
                
                    with open("finalsmovies.csv",encoding='utf-8') as file:
                            reader = csv.reader(file)
                            # skip the first row, since it is header.
                            header = next(reader)
                            found = False
                            count = 0
                            for line in reader:
                                try:
                                    if int(line[2]) >=tvyear1:
                                        print("\nTconst :",line[0])
                                        print("\nmovie name :",line[1])
                                        print("\nReleased Year :",line[2])
                                        print("\nGenre :",line[3])
                                        print("\nLanguage :",line[4])
                                        print("\nDirector :",line[5])
                                        print("\nActors :",line[6])
                                        print("\nRating :",line[7])
                                        found = True
                                        print("\n\\N indicates that the data has not been loaded\n")
                                        count+=1
                                except Exception:
                                    pass
                            print("Matches found :"+str(count))
                            print('Do you want to save it in a csv file? [1/0]')
                            save=int(input())
                            if(save == 1 ):
                                with open("finalsmovies.csv",encoding='utf-8') as file:
                                    reader = csv.reader(file)
                            # skip the first row, since it is header.
                                    header = next(reader)
                                    tv_yearmovie=open("tvyear_"+str(tvyear1)+".csv","w",newline="")
                                    writer=csv.writer(tv_yearmovie)
                                    writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"]
            )
                                    for line in reader:
                                        try:
                                            if int(line[2]) >=tvyear1:
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                        except Exception:
                                            pass
                                    print('Check in the current directory for the csv file')
                            else:
                                    print('Ok')
                            if not found:
                                print("not found") 
                elif(choiceyear==5):
                    tvyear1=int(input("Enter the year:"))
                
                    with open("finalsmovies.csv",encoding='utf-8') as file:
                            reader = csv.reader(file)
                            # skip the first row, since it is header.
                            header = next(reader)
                            found = False
                            count = 0
                            for line in reader:
                                try:
                                    if int(line[2]) <=tvyear1:
                                        print("\nTconst :",line[0])
                                        print("\nmovie name :",line[1])
                                        print("\nReleased Year :",line[2])
                                        print("\nGenre :",line[3])
                                        print("\nLanguage :",line[4])
                                        print("\nDirector :",line[5])
                                        print("\nActors :",line[6])
                                        print("\nRating :",line[7])
                                        found = True
                                        print("\n\\N indicates that the data has not been loaded\n")
                                        count+=1
                                except Exception:
                                    pass
                            print("Matches found :"+str(count))
                            print('Do you want to save it in a csv file? [1/0]')
                            save=int(input())
                            if(save == 1 ):
                                with open("finalsmovies.csv",encoding='utf-8') as file:
                                    reader = csv.reader(file)
                            # skip the first row, since it is header.
                                    header = next(reader)
                                    tv_yearmovie=open("tvyear_"+str(tvyear1)+".csv","w",newline="")
                                    writer=csv.writer(tv_yearmovie)
                                    writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"]
            )
                                    for line in reader:
                                        try:
                                            if int(line[2]) <=tvyear1:
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                        except Exception:
                                                pass
                                    print('Check in the current directory for the csv file')
                            else:
                                    print('Ok')
                            if not found:
                                print("not found")
                elif(choiceyear==0):
                     print('\n\033[91m'+'\nExiting...\n'+'\n\033[91m')
                     break
                else:
                    print("PLEASE ENTER A CORRECT OPTION !!")
                              
                    
        elif(choice==3):
            director = input("""Enter the name of director to search : """)
            start = time.time()
            with open("finalsmovies.csv",errors='ignore') as file:
                reader = csv.reader(file)
            # skip the first row, since it is header.
                header = next(reader)
                found = False
                count=0
            
                for line in reader:
                
                    regex = re.compile(".*("+director+").*",re.I)
                    try:
                        if regex.findall(line[5]):
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
                start = time.time()
                with open("finalsmovies.csv",encoding='utf-8') as file:
                        reader = csv.reader(file)
                # skip the first row, since it is header.
                        header = next(reader)
                        tv_yearseries=open("movie_"+str(director)+".csv","w",newline="")
                        writer=csv.writer(tv_yearseries)
                        writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
                        for line in reader:
                                try:
                                        if regex.findall(line[5]):
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                except Exception:
                                        pass
                        print('Check in the current directory for the csv file')
                        end=time.time()
                        print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
            else:
                    print('Ok')
                
                
            if not found:
                print(director, "not found")
        elif(choice==4):
            actor = input("""Enter the name of actor to search : """)
            start = time.time()
            with open("finalsmovies.csv",errors='ignore') as file:
                reader = csv.reader(file)
            # skip the first row, since it is header.
                header = next(reader)
                found = False
                count=0
            
                for line in reader:
                
                    regex = re.compile(".*("+actor+").*",re.I)
                    try:
                        if regex.findall(line[6]):
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
                start = time.time()
                with open("finalsmovies.csv",encoding='utf-8') as file:
                        reader = csv.reader(file)
                # skip the first row, since it is header.
                        header = next(reader)
                        tv_yearseries=open("movie_"+str(actor)+".csv","w",newline="")
                        writer=csv.writer(tv_yearseries)
                        writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
                        for line in reader:
                                try:
                                        if regex.findall(line[6]):
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                except Exception:
                                        pass
                        print('Check in the current directory for the csv file')
                        end=time.time()
                        print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
            else:
                    print('Ok')
                
                
            if not found:
                print(actor, "not found")
        elif(choice==5):
            start = time.time()
            language = input("""Enter the name of language to search : """)

            with open("finalsmovies.csv",errors='ignore') as file:
                reader = csv.reader(file)
            # skip the first row, since it is header.
                header = next(reader)
                found = False
                count=0
            
                for line in reader:
                
                    regex = re.compile(".*("+language+").*",re.I)
                    try:
                        if regex.findall(line[4]):
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
                start = time.time()
                with open("finalsmovies.csv",encoding='utf-8') as file:
                        reader = csv.reader(file)
                # skip the first row, since it is header.
                        header = next(reader)
                        tv_yearseries=open("movie_"+str(language)+".csv","w",newline="")
                        writer=csv.writer(tv_yearseries)
                        writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
                        for line in reader:
                                try:
                                        if regex.findall(line[4]):
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                except Exception:
                                        pass
                        print('Check in the current directory for the csv file')
                        end=time.time()
                        print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
            else:
                    print('Ok')
                
                
            if not found:
                print(language, "not found")
        elif(choice ==6):
            
            genre= str(input("Enter the Genre :"))
            start = time.time()
            with open("finalsmovies.csv",encoding='utf-8') as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                count=0
                for line in reader:
                    start=time.time()
                    regex = re.compile(".*("+genre+").*",re.I)
                    try:
                        if regex.findall(line[3]):
                            print("\nTconst :",line[0])
                            print("\nmovie name :",line[1])
                            print("\nReleased Year :",line[2])
                            print("\nGenre :",line[3])
                            print("\nLanguage :",line[4])
                            print("\nDirector :",line[5])
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
                    start = time.time()
                    with open("finalsmovies.csv",encoding='utf-8') as file:
                        reader = csv.reader(file)
                # skip the first row, since it is header.
                        header = next(reader)
                        tv_yearmovie=open("movie_"+genre+".csv","w",newline="")
                        writer=csv.writer(tv_yearmovie)
                        writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
                        for line in reader:
                            try:
                                if regex.findall(line[3]):
                                    writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                            except Exception:
                                pass
                        print('Check in the current directory for the csv file')
                        end=time.time()
                        print('Completed the task in',"{0:.2f}".format(end-start)+" seconds")
                else:
                    print('Ok')        
                if not found:
                    print(genre, " is not found")

        elif(choice==7):
            print("\nPRESS 1 to obtain all the movie based ona particular rating")
            print("PRESS 2 to obtain all the movie between 2 ratings of your choice")
            print("PRESS 3 to obtain all the movie which is greater than a rating of your choice")
            print("PRESS 4 to obtain all the movie which is less than a rating of your choice\n")
            print("PRESS 0 to exit")
            choicerating=int(input())
            if(choicerating==1):
                movierating=float(input("Enter the  rating "))
                with open("finalsmovies.csv",encoding='utf-8') as file:
                    reader = csv.reader(file)
                    # skip the first row, since it is header.
                    header = next(reader)
                    found = False
                    count = 0
                    
                    for line in reader:
                        try:
                            if line[-1]!='\\N':
                            
                                if float(line[-1])== movierating :
                                    print("\nTconst :",line[0])
                                    print("\nmovie name :",line[1])
                                    print("\nReleased Year :",line[2])
                                    print("\nGenre :",line[3])
                                    print("\nLanguage :",line[4])
                                    print("\nDirector :",line[5])
                                    print("\nActors :",line[6])
                                    print("\nRating :",line[7])
                                    found = True
                                    print("\n\\N indicates that the data has not been loaded\n")
                                    count+=1
                        except Exception:
                            pass
                    print("Matches found :"+str(count))
                    print('Do you want to save it in a csv file? [1/0]')
                    save=int(input())
                    if(save == 1 ):
                        with open("finalsmovies.csv",encoding='utf-8') as file:
                                reader = csv.reader(file)
                        # skip the first row, since it is header.
                                header = next(reader)
                                tv_yearmovie=open("movierating_"+str(movierating)+".csv","w",newline="")
                                writer=csv.writer(tv_yearmovie)
                                writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
                                for line in reader:
                                    try:
                                        if line[-1]!='\\N':
                                            if float(line[-1]) == movierating:
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                    except Exception:
                                         pass
                                print('Check in the current directory for the csv file')
                    else:
                        print('Ok')
                    if not found:
                        print("not found")
                    
                
            elif(choicerating==2):
                movierating=float(input("Enter the from rating to start with:"))
                tvrating2=float(input("Enter the to rating :"))
                
                with open("finalsmovies.csv",encoding='utf-8') as file:
                    reader = csv.reader(file)
                    # skip the first row, since it is header.
                    header = next(reader)
                    found = False
                    count = 0
                    
                    for line in reader:
                        try:
                            if line[-1]!='\\N':
                            
                                if float(line[-1])>= movierating and float(line[-1]) <= tvrating2 :
                                    print("\nTconst :",line[0])
                                    print("\nmovie name :",line[1])
                                    print("\nReleased Year :",line[2])
                                    print("\nGenre :",line[3])
                                    print("\nLanguage :",line[4])
                                    print("\nDirector :",line[5])
                                    print("\nActors :",line[6])
                                    print("\nRating :",line[7])
                                    found = True
                                    print("\n\\N indicates that the data has not been loaded\n")
                                    count+=1
                        except Exception:
                            pass
                    print("Matches found :"+str(count))
                    print('Do you want to save it in a csv file? [1/0]')
                    save=int(input())
                    if(save == 1 ):
                        with open("finalsmovies.csv",encoding='utf-8') as file:
                                reader = csv.reader(file)
                        # skip the first row, since it is header.
                                header = next(reader)
                                tv_yearmovie=open("movierating_"+str(movierating)+" to "+str(tvrating2)+".csv","w",newline="")
                                writer=csv.writer(tv_yearmovie)
                                writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
                                for line in reader:
                                    try:
                                        if line[-1]!='\\N':
                                            if float(line[-1]) > movierating and float(line[-1]) <= tvrating2 :
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                    except Exception:
                                         pass
                                print('Check in the current directory for the csv file')
                    else:
                        print('Ok')
                    if not found:
                        print("not found")
            elif(choicerating==3):
                movierating=float(input("Enter the from rating to start with:"))

                
                with open("finalsmovies.csv",encoding='utf-8') as file:
                    reader = csv.reader(file)
                    # skip the first row, since it is header.
                    header = next(reader)
                    found = False
                    count = 0
                    
                    for line in reader:
                        try:
                            if line[-1]!='\\N':
                            
                                if float(line[-1])>= movierating :
                                    print("\nTconst :",line[0])
                                    print("\nmovie name :",line[1])
                                    print("\nReleased Year :",line[2])
                                    print("\nGenre :",line[3])
                                    print("\nLanguage :",line[4])
                                    print("\nDirector :",line[5])
                                    print("\nActors :",line[6])
                                    print("\nRating :",line[7])
                                    found = True
                                    print("\n\\N indicates that the data has not been loaded\n")
                                    count+=1
                        except Exception:
                            pass
                    print("Matches found :"+str(count))
                    print('Do you want to save it in a csv file? [1/0]')
                    save=int(input())
                    if(save == 1 ):
                        with open("finalsmovies.csv",encoding='utf-8') as file:
                                reader = csv.reader(file)
                        # skip the first row, since it is header.
                                header = next(reader)
                                tv_yearmovie=open("movierating_"+str(movierating)+".csv","w",newline="")
                                writer=csv.writer(tv_yearmovie)
                                writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
                                for line in reader:
                                    try:
                                        if line[-1]!='\\N':
                                            if float(line[-1]) >= movierating:
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                    except Exception:
                                         pass
                                print('Check in the current directory for the csv file')
                    else:
                        print('Ok')
                    if not found:
                        print("not found")
            elif(choicerating==4):
                movierating=float(input("Enter the from rating to start with:"))

                
                with open("finalsmovies.csv",encoding='utf-8') as file:
                    reader = csv.reader(file)
                    # skip the first row, since it is header.
                    header = next(reader)
                    found = False
                    count = 0
                    
                    for line in reader:
                        try:
                            if line[-1]!='\\N':
                            
                                if float(line[-1])<= movierating :
                                    print("\nTconst :",line[0])
                                    print("\nmovie name :",line[1])
                                    print("\nReleased Year :",line[2])
                                    print("\nGenre :",line[3])
                                    print("\nLanguage :",line[4])
                                    print("\nDirector :",line[5])
                                    print("\nActors :",line[6])
                                    print("\nRating :",line[7])
                                    found = True
                                    print("\n\\N indicates that the data has not been loaded\n")
                                    count+=1
                        except Exception:
                            pass
                    print("Matches found :"+str(count))
                    print('Do you want to save it in a csv file? [1/0]')
                    save=int(input())
                    if(save == 1 ):
                        with open("finalsmovies.csv",encoding='utf-8') as file:
                                reader = csv.reader(file)
                        # skip the first row, since it is header.
                                header = next(reader)
                                tv_yearmovie=open("movierating_"+str(movierating)+".csv","w",newline="")
                                writer=csv.writer(tv_yearmovie)
                                writer.writerow(["tconst","primarytitle","year","genre","language","directors","actors","avg_rating"])
                                for line in reader:
                                    try:
                                        if line[-1]!='\\N':
                                            if float(line[-1]) <= movierating:
                                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                                    except Exception:
                                        pass
                                print('Check in the current directory for the csv file')
                    else:
                        print('Ok')
                    if not found:
                        print("not found")
            elif(choice==0):
                    print('\n\033[91m'+'\nExiting...\n'+'\n\033[91m')
                    break
            else:
                    print("PLEASE ENTER A CORRECT OPTION !!")
        elif(choice==0):
                print('\n\033[91m'+'\nExiting...\n'+'\n\033[91m')
                break
        else:
                print("PLEASE ENTER A CORRECT OPTION !!")