import csv
import time
import re
import pandas as pd
def selectivesearch_series():
    print("PRESS 1 to search a particular series by its title")
    print("PRESS 2 to Search the series according to start year")
    print("PRESS 3 to Search the series by its genre")
    print("PRESS 4 to Search by rating:")
    choice=int(input())
    if(choice==1):
        tvseries= str(input("Enter the name of tv series you want to find :"))
        with open("finalseries.csv") as file:
            reader = csv.reader(file)
            # skip the first row, since it is header.
            header = next(reader)
            found = False
            count=0
            for line in reader:
                regex = re.compile(".*("+tvseries+").*",re.I)
                if regex.findall(line[1]):
                    print("\nTconst :",line[0])
                    print("\nTv series name :",line[1])
                    print("\nStart Year :",line[2])
                    print("\nEnd Year :",line[3])
                    print("\nRun time :",line[4])
                    print("\nGenre:",line[5])
                    print("\nNumber of Votes :",line[6])
                    print("\nRating :",line[7])
                    found = True
                    print("\n\\N indicates that the data has not been loaded\n")
                    count+=1
                    
            if not found:
                print(tvseries, " is not found")

        print("Matches found :"+str(count))
    elif(choice == 2):
        print("PRESS 1 to Search all series according to one particular start year")
        print("PRESS 2 to Search the series by its title and its start year")
        print("PRESS 3 to Search all the series present between two years of your choice")
        print("PRESS 4 to Search all the series started after a  particular year")
        print("PRESS 5 to Search all the series started before a  particular year")
        choiceyear=int(input())
        if(choiceyear==1):
            
            tvyear=str(input("Enter the start year  :"))
            with open("finalseries.csv") as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                count = 0
                for line in reader:
                    if line[2] ==tvyear :
                        print("\nTconst :",line[0])
                        print("\nTv series name :",line[1])
                        print("\nStart Year :",line[2])
                        print("\nEnd Year :",line[3])
                        print("\nRun time :",line[4])
                        print("\nGenre:",line[5])
                        print("\nNumber of Votes :",line[6])
                        print("\nRating :",line[7])
                        found = True
                        print("\n\\N indicates that the data has not been loaded\n")
                        count+=1
                print("Matches found :"+str(count))
                print('Do you want to save it in a csv file? [1/0]')
                save=int(input())
                if(save == 1 ):
                    with open("finalseries.csv") as file:
                        reader = csv.reader(file)
                # skip the first row, since it is header.
                        header = next(reader)
                        tv_yearseries=open("tvyear_"+str(tvyear)+".csv","w",newline="")
                        writer=csv.writer(tv_yearseries)
                        writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                        for line in reader:
                            if line[2]==tvyear:
                                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                        print('Check in the current directory for the csv file')
                else:
                    print('Ok')
                if not found:
                    print("not found")
        elif(choiceyear==2):
            
            tvseries = str(input("Enter the name of tv series you want to find :"))
            tvyear=str(input("Enter the start year of that tv series :"))
            with open("finalseries.csv") as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                for line in reader:
                    regex = re.compile(".*("+tvseries+").*",re.I)
                    if line[2] == tvyear and regex.findall(line[1]):
                        print("\nTconst :",line[0])
                        print("\nTv series name :",line[1])
                        print("\nStart Year :",line[2])
                        print("\nEnd Year :",line[3])
                        print("\nRun time :",line[4])
                        print("\nGenre:",line[5])
                        found = True
                        print("\n\\N indicates that the data has not been loaded\n")
                    
                if not found:
                    print("not found")
                    
        elif(choiceyear==3):
            tvyear1=int(input("Enter the from year to start with:"))
            tvyear2=int(input("Enter the to year :"))
        
            with open("finalseries.csv") as file:
                    reader = csv.reader(file)
                    # skip the first row, since it is header.
                    header = next(reader)
                    found = False
                    count = 0
                    for line in reader:
                        if int(line[2]) >=tvyear1 and int(line[2]) <= tvyear2 :
                            print("\nTconst :",line[0])
                            print("\nTv series name :",line[1])
                            print("\nStart Year :",line[2])
                            print("\nEnd Year :",line[3])
                            print("\nRun time :",line[4])
                            print("\nGenre:",line[5])
                            print("\nNumber of Votes :",line[6])
                            print("\nRating :",line[7])
                            found = True
                            print("\n\\N indicates that the data has not been loaded\n")
                            count+=1
                    print("Matches found :"+str(count))
                    print('Do you want to save it in a csv file? [1/0]')
                    save=int(input())
                    if(save == 1 ):
                        with open("finalseries.csv") as file:
                            reader = csv.reader(file)
                    # skip the first row, since it is header.
                            header = next(reader)
                            tv_yearseries=open("tvyear_"+str(tvyear1)+" to "+str(tvyear2)+".csv","w",newline="")
                            writer=csv.writer(tv_yearseries)
                            writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                            for line in reader:
                                if int(line[2]) >=tvyear1 and int(line[2]) <= tvyear2 :
                                    writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                            print('Check in the current directory for the csv file')
                    else:
                            print('Ok')
                    if not found:
                        print("not found")
                        
        elif(choiceyear==4):
            tvyear1=int(input("Enter the year:"))
        
            with open("finalseries.csv") as file:
                    reader = csv.reader(file)
                    # skip the first row, since it is header.
                    header = next(reader)
                    found = False
                    count = 0
                    for line in reader:
                        if int(line[2]) >=tvyear1:
                            print("\nTconst :",line[0])
                            print("\nTv series name :",line[1])
                            print("\nStart Year :",line[2])
                            print("\nEnd Year :",line[3])
                            print("\nRun time :",line[4])
                            print("\nGenre:",line[5])
                            print("\nNumber of Votes :",line[6])
                            print("\nRating :",line[7])
                            found = True
                            print("\n\\N indicates that the data has not been loaded\n")
                            count+=1
                    print("Matches found :"+str(count))
                    print('Do you want to save it in a csv file? [1/0]')
                    save=int(input())
                    if(save == 1 ):
                        with open("finalseries.csv") as file:
                            reader = csv.reader(file)
                    # skip the first row, since it is header.
                            header = next(reader)
                            tv_yearseries=open("tvyear_"+str(tvyear1)+".csv","w",newline="")
                            writer=csv.writer(tv_yearseries)
                            writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                            for line in reader:
                                if int(line[2]) >=tvyear1:
                                    writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                            print('Check in the current directory for the csv file')
                    else:
                            print('Ok')
                    if not found:
                        print("not found") 
        elif(choiceyear==5):
            tvyear1=int(input("Enter the year:"))
        
            with open("finalseries.csv") as file:
                    reader = csv.reader(file)
                    # skip the first row, since it is header.
                    header = next(reader)
                    found = False
                    count = 0
                    for line in reader:
                        if int(line[2]) <=tvyear1:
                            print("\nTconst :",line[0])
                            print("\nTv series name :",line[1])
                            print("\nStart Year :",line[2])
                            print("\nEnd Year :",line[3])
                            print("\nRun time :",line[4])
                            print("\nGenre:",line[5])
                            print("\nNumber of Votes :",line[6])
                            print("\nRating :",line[7])
                            found = True
                            print("\n\\N indicates that the data has not been loaded\n")
                            count+=1
                    print("Matches found :"+str(count))
                    print('Do you want to save it in a csv file? [1/0]')
                    save=int(input())
                    if(save == 1 ):
                        with open("finalseries.csv") as file:
                            reader = csv.reader(file)
                    # skip the first row, since it is header.
                            header = next(reader)
                            tv_yearseries=open("tvyear_"+str(tvyear1)+".csv","w",newline="")
                            writer=csv.writer(tv_yearseries)
                            writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                            for line in reader:
                                if int(line[2]) <=tvyear1:
                                    writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                            print('Check in the current directory for the csv file')
                    else:
                            print('Ok')
                    if not found:
                        print("not found")          
                

    elif(choice ==3):
        genre= str(input("Enter the Genre :"))
        with open("finalseries.csv") as file:
            reader = csv.reader(file)
            # skip the first row, since it is header.
            header = next(reader)
            found = False
            count=0
            for line in reader:
                start=time.time()
                regex = re.compile(".*("+genre+").*",re.I)
                if regex.findall(line[5]):
                    print("\nTconst :",line[0])
                    print("\nTv series name :",line[1])
                    print("\nStart Year :",line[2])
                    print("\nEnd Year :",line[3])
                    print("\nRun time :",line[4])
                    print("\nGenre:",line[5])
                    print("\nNumber of Votes :",line[6])
                    print("\nRating :",line[7])
                    found = True
                    print("\n\\N indicates that the data has not been loaded\n")
                    count+=1
                
            print("Matches found :"+str(count))
            print('Do you want to save it in a csv file? [1/0]')
            save=int(input())
            if(save == 1 ):
                with open("finalseries.csv") as file:
                    reader = csv.reader(file)
            # skip the first row, since it is header.
                    header = next(reader)
                    tv_yearseries=open("tv_"+genre+".csv","w",newline="")
                    writer=csv.writer(tv_yearseries)
                    writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                    for line in reader:
                        if regex.findall(line[5]):
                            writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                    print('Check in the current directory for the csv file')
            else:
                print('Ok')        
            if not found:
                print(genre, " is not found")

    elif(choice==4):
        print("PRESS 1 to search all the series based ona particular rating")
        print("PRESS 2 to search all the series between 2 ratings of your choice")
        print("PRESS 3 to search all the series which is greater than a rating of your choice")
        print("PRESS 4 to search all the series which is less than a rating of your choice")
        choicerating=int(input())
        if(choicerating==1):
            tvrating1=float(input("Enter the  rating "))
            with open("finalseries.csv") as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                count = 0
                
                for line in reader:
                    if line[-1]!='\\N':
                    
                        if float(line[-1])== tvrating1 :
                            print("\nTconst :",line[0])
                            print("\nTv series name :",line[1])
                            print("\nStart Year :",line[2])
                            print("\nEnd Year :",line[3])
                            print("\nRun time :",line[4])
                            print("\nGenre:",line[5])
                            print("\nNumber of Votes :",line[6])
                            print("\nRating :",line[7])
                            found = True
                            print("\n\\N indicates that the data has not been loaded\n")
                            count+=1
                print("Matches found :"+str(count))
                print('Do you want to save it in a csv file? [1/0]')
                save=int(input())
                if(save == 1 ):
                    with open("finalseries.csv") as file:
                            reader = csv.reader(file)
                    # skip the first row, since it is header.
                            header = next(reader)
                            tv_yearseries=open("tvrating_"+str(tvrating1)+".csv","w",newline="")
                            writer=csv.writer(tv_yearseries)
                            writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                            for line in reader:
                                if line[-1]!='\\N':
                                    if float(line[-1]) == tvrating1:
                                        writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                            print('Check in the current directory for the csv file')
                else:
                    print('Ok')
                if not found:
                    print("not found")
                
            
        elif(choicerating==2):
            tvrating1=float(input("Enter the from rating to start with:"))
            tvrating2=float(input("Enter the to rating :"))
            
            with open("finalseries.csv") as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                count = 0
                
                for line in reader:
                    if line[-1]!='\\N':
                    
                        if float(line[-1])>= tvrating1 and float(line[-1]) <= tvrating2 :
                            print("\nTconst :",line[0])
                            print("\nTv series name :",line[1])
                            print("\nStart Year :",line[2])
                            print("\nEnd Year :",line[3])
                            print("\nRun time :",line[4])
                            print("\nGenre:",line[5])
                            print("\nNumber of Votes :",line[6])
                            print("\nRating :",line[7])
                            found = True
                            print("\n\\N indicates that the data has not been loaded\n")
                            count+=1
                print("Matches found :"+str(count))
                print('Do you want to save it in a csv file? [1/0]')
                save=int(input())
                if(save == 1 ):
                    with open("finalseries.csv") as file:
                            reader = csv.reader(file)
                    # skip the first row, since it is header.
                            header = next(reader)
                            tv_yearseries=open("tvrating_"+str(tvrating1)+" to "+str(tvrating2)+".csv","w",newline="")
                            writer=csv.writer(tv_yearseries)
                            writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                            for line in reader:
                                if line[-1]!='\\N':
                                    if float(line[-1]) > tvrating1 and float(line[-1]) <= tvrating2 :
                                        writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                            print('Check in the current directory for the csv file')
                else:
                    print('Ok')
                if not found:
                    print("not found")
        elif(choicerating==3):
            tvrating1=float(input("Enter the from rating to start with:"))

            
            with open("finalseries.csv") as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                count = 0
                
                for line in reader:
                    if line[-1]!='\\N':
                    
                        if float(line[-1])>= tvrating1 :
                            print("\nTconst :",line[0])
                            print("\nTv series name :",line[1])
                            print("\nStart Year :",line[2])
                            print("\nEnd Year :",line[3])
                            print("\nRun time :",line[4])
                            print("\nGenre:",line[5])
                            print("\nNumber of Votes :",line[6])
                            print("\nRating :",line[7])
                            found = True
                            print("\n\\N indicates that the data has not been loaded\n")
                            count+=1
                print("Matches found :"+str(count))
                print('Do you want to save it in a csv file? [1/0]')
                save=int(input())
                if(save == 1 ):
                    with open("finalseries.csv") as file:
                            reader = csv.reader(file)
                    # skip the first row, since it is header.
                            header = next(reader)
                            tv_yearseries=open("tvrating_"+str(tvrating1)+".csv","w",newline="")
                            writer=csv.writer(tv_yearseries)
                            writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                            for line in reader:
                                if line[-1]!='\\N':
                                    if float(line[-1]) >= tvrating1:
                                        writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                            print('Check in the current directory for the csv file')
                else:
                    print('Ok')
                if not found:
                    print("not found")
        elif(choicerating==4):
            tvrating1=float(input("Enter the from rating to start with:"))

            
            with open("finalseries.csv") as file:
                reader = csv.reader(file)
                # skip the first row, since it is header.
                header = next(reader)
                found = False
                count = 0
                
                for line in reader:
                    if line[-1]!='\\N':
                    
                        if float(line[-1])<= tvrating1 :
                            print("\nTconst :",line[0])
                            print("\nTv series name :",line[1])
                            print("\nStart Year :",line[2])
                            print("\nEnd Year :",line[3])
                            print("\nRun time :",line[4])
                            print("\nGenre:",line[5])
                            print("\nNumber of Votes :",line[6])
                            print("\nRating :",line[7])
                            found = True
                            print("\n\\N indicates that the data has not been loaded\n")
                            count+=1
                print("Matches found :"+str(count))
                print('Do you want to save it in a csv file? [1/0]')
                save=int(input())
                if(save == 1 ):
                    with open("finalseries.csv") as file:
                            reader = csv.reader(file)
                    # skip the first row, since it is header.
                            header = next(reader)
                            tv_yearseries=open("tvrating_"+str(tvrating1)+".csv","w",newline="")
                            writer=csv.writer(tv_yearseries)
                            writer.writerow(["tconst","primarytitle","startYear","endYear","runtimeMinutes","genres","averagevotes","rating"])
                            for line in reader:
                                if line[-1]!='\\N':
                                    if float(line[-1]) <= tvrating1:
                                        writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]])
                            print('Check in the current directory for the csv file')
                else:
                    print('Ok')
                if not found:
                    print("not found")