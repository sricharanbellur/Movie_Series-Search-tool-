import csv 
from deleteprimary_movies import deleteprimary
from deletesecondary_movies import deletesecondary
from deleteprimary_series import deleteprimaryseries
from deletesecondary_series import deletesecondaryseries
from insert_primarymovies import insert_movie
from selectivesearch_movies import selectivesearch_movie
from primarykeyindexing_movies import primarykey_movie
from primarysearch_movies import primarysearch_movie
from secondarykeyindexing_movies import secondarykey_movie
from secondarysearch_movies import secondarysearch_movie
from insert_series import insert_series
from primarykeyindexing_series import primarykey_series
from primarysearch_series import primarysearch_series
from secondarykeyindexing_series import secondarykey_series
from secondarysearch_series import secondarysearch_series
from selectivesearch_series import selectivesearch_series
print('\033[93m'+"\n--------------WELCOME TO MOVIE-TVSERIES SEARCH TOOL--------------\n"+'\033[93m')

while True:
    choice=int(input('\033[96m'+" PRESS 1 FOR MOVIES\n PRESS 2 FOR TV SERIES\n PRESS 0 FOR EXIT\n "+'\033[96m'))
    if(choice==1):
        while True:
            print('\n\033[36m'+"PRESS 1 TO SEARCH AND OBTAIN MOVIES"+'\033[36m')
            print('\033[36m'+"PRESS 2 TO IMPLEMENT PRIMARY KEY INDEXING ON MOVIES"+'\033[36m')
            print('\033[36m'+"PRESS 3 TO SEARCH MOVIES USING PRIMARY KEY"+'\033[36m')
            print('\033[36m'+"PRESS 4 TO IMPLEMENT SECONDARY KEY INDEXING ON MOVIES"+'\033[36m')
            print('\033[36m'+"PRESS 5 TO SEARCH MOVIES USING SECONDARY KEY"+'\033[36m')
            print('\033[36m'+"PRESS 6 TO INSERT A MOVIE TO DATASET"+'\033[36m')
            print('\033[36m'+"PRESS 7 TO DELETE A MOVIE FROM DATASET USING PRIMARY KEY"+'\033[36m')
            print('\033[36m'+"PRESS 8 TO DELETE A MOVIE FROM DATASET USING SECONDARY KEY"+'\033[36m\n')
            print('\033[36m'+"PRESS 0 TO EXIT "+'\033[36m\n')
            moviechoice=int(input())
            if(moviechoice==1):
                selectivesearch_movie();
            elif(moviechoice==2):
                primarykey_movie();
            elif(moviechoice==3):
                primarysearch_movie();
            elif(moviechoice==4):
                secondarykey_movie();
            elif(moviechoice==5):
                secondarysearch_movie();
            elif(moviechoice==6):
                insert_movie();
            elif(moviechoice==7):
                deleteprimary()
            elif(moviechoice==8):
                deletesecondary()
            elif(moviechoice==0):
                print('\n\033[91m'+'\nExiting...\n'+'\n\033[91m')
                break
            else:
                print("PLEASE ENTER A CORRECT OPTION !!")
    elif(choice==2):
        while True:
            print('\n\033[36m'+"PRESS 1 TO SEARCH AND OBTAIN TV-SERIES"+'\033[36m')
            print('\033[36m'+"PRESS 2 TO IMPLEMENT PRIMARY KEY INDEXING ON TV-SERIES"+'\033[36m')
            print('\033[36m'+"PRESS 3 TO SEARCH TV-SERIES USING PRIMARY KEY"+'\033[36m')
            print('\033[36m'+"PRESS 4 TO IMPLEMENT SECONDARY KEY INDEXING ON TV-SERIES"+'\033[36m')
            print('\033[36m'+"PRESS 5 TO SEARCH TV-SERIES USING SECONDARY KEY"+'\033[36m')
            print('\033[36m'+"PRESS 6 TO INSERT A TV-SERIES TO DATASET"+'\033[36m')
            print('\033[36m'+"PRESS 7 TO DELETE A TV-SERIES FROM DATASET USING PRIMARY KEY"+'\033[36m')
            print('\033[36m'+"PRESS 8 TO DELETE A TV-SERIES FROM DATASET USING SECONDARY KEY"+'\033[36m\n')
            print('\033[36m'+"PRESS 0 TO EXIT "+'\033[36m\n')
            serieschoice=int(input())
            if(serieschoice==0):
                print('\n\033[91m'+'\nExiting...\n'+'\n\033[91m')
                break
            elif(serieschoice ==1):
                selectivesearch_series();
            elif(serieschoice ==2):
                primarykey_series();
            elif(serieschoice ==3):
                primarysearch_series();
            elif(serieschoice ==4):
                secondarykey_series()
            elif(serieschoice ==5):
                secondarysearch_series()
            elif(serieschoice ==6):
                insert_series();
            elif(serieschoice==7):
                deleteprimaryseries()
            elif(serieschoice==8):
                deletesecondaryseries()
            else:
                print("PLEASE ENTER A CORRECT OPTION !!")
    elif(choice==0):
        print('\n\033[91m'+'\nExiting...'+'\n\033[91m')
        exit()
    else:
        print('\n\033[91m'+'INVALID OPTION'+'\033[91m\n')
       