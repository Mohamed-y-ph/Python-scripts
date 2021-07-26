

'''import the required libraries needed for running the program without errors'''
import pandas as pd
import time
import numpy as np
print('\nWelcome to this program which was designed by Mohamed Yaser to compute some statistics about bikeshare\n')
print("Which city do you want to deal with? Washington, New York, or Chicago?")
cities={ 'c': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }
def filter_data(file):
    try:
        month=input('\nPlease enter the first 3 letters of the month you want to filter (e.g. Feb,Mar...etc), or type all\nYour answer: ').lower()
        day=input('\nPlease enter the day you want to filter (e.g. Saturday,Sunday...etc), or type all\nYour answer: ')
        file = pd.read_csv(cities[city])
        file['Start Time'] = pd.to_datetime(file['Start Time'])
        # extract month and day of week from Start Time to create new columns
        file['Month'] = file['Start Time'].dt.month
        file['Weekday'] = file['Start Time'].dt.day_name()
        if month != 'all':
            months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
            month = months.index(month) + 1
            file = file[file['Month'] == month]
        if day != 'all':
            file = file[file['Weekday'] == day.title()]

        print (file)
    except:
        print('This is not a valid response')

def view_data(file):
    view_data = input('\nWould you like to view the first 5 rows of data?\nEnter (y/n): ').lower()
    start_loc = 5
    while (view_data=='y'):
      print(file.iloc[0:start_loc])
      start_loc += 5
      view_data = input("Do you want to show more five rows? (y/n):  ").lower()

def most_popular_month(x):
    try:
        pm = pd.to_datetime(x['Start Time']).dt.month.mode()[0]
        print('-'*20,'\nThe most popular month is: ', pm)
    except:
        print('\nOops!!\nIt seems that this is not the correct name')

def most_popular_day(file):
    '''Calculates the most popular day'''
    try:
        pdd = pd.to_datetime(file['Start Time']).dt.day.mode()[0]
        print('-'*20,'\nThe most popular day is: ', pdd, '\n')
    except:
        print('\nThis is not the right name of the column (Please consider upper and lower case)')

def most_popular_hour(file):
    '''This function calculates the most popular hour based on the column containing the start times details,
    (inp) reads the name of the time column from the user, and (pw) extracts hours from the start time column in order to calculate the most frequent hour'''
    try:
        pw = pd.to_datetime(file['Start Time']).dt.hour.mode()[0]
        print('-'*20,'\nThe most crowded hour is: ', pw, '\n')
    except:
        print('This is not the right name of the column (Please consider upper and lower case)')

def most_ststaion(file):
    '''This function calulates the most common start station
    (s)states for the name of the column containg the start station name, and (ss) states for the most common start station'''
    try:
        s = input('\nPlease enter the name of the column containg the start station in the file: ')
        ss=file[s].mode()[0]
        print('-'*20,'\nThe most common start station is', ss)
    except:
        print('This is not the right name of the column (Please consider upper and lower case)')
def most_enstation(file):
    '''This function calculates the most common end station'''
    try:
        endstation = input('\nPlease enter the name of the column containg the end station in the file: ')
        most_common=file[endstation].mode()[0]
        print('-'*20,'\nThe most common end station is ',most_common)
    except:
        print('This is not the right name of the column (Please consider upper and lower case)')

def most_cotrip(file):
    '''Calulates the most common trip based on the user inputs'''
    try:
        starttime=input('\nPlease enter the name of the column containg the start station in the file: ')
        endtime=input('\nPlease enter the name of the column containg the end station in the file: ')
        most_common_trip=(file[starttime]+' to '+file[endtime]).mode()[0]
        print('-'*20,'\nThe most common trip is from',most_common_trip)
    except:
        print('This is not the right name of the column (Please consider upper and lower case)')
def total_travel_time(file):
    '''This function computes the total travel time in hours and minutes, (st) computes the total hours and (sm) computes the total minutes'''
    try:
        #starttime=input('\nPlease enter the name of the start time column: ')
        #endtime=input('\nPlease enter the name of the end time column: ')
        st=sum(pd.to_datetime(file['End Time']).dt.hour -pd.to_datetime(file['Start Time']).dt.hour)
        sm=sum(pd.to_datetime(file['End Time']).dt.minute -pd.to_datetime(file['Start Time']).dt.minute)
        print('-'*20,'\nThe total travel time is ',st,'hours and',sm,'minutes')
    except:
        print('This is not the right name of the column (Please consider upper and lower case)')
def average_travel_time(file):
    '''This function calculates the mean of the travel times'''
    try:
        #s = input('\nPlease enter the name of the start time column: ')
        #e = input('\nPlease enter the name of the end time column: ')
        st = (pd.to_datetime(file['End Time'])) - (pd.to_datetime(file['Start Time']))
        print('\nThe total travel time is', np.mean(st))
    except:
        print('This is not the right name of the column (Please consider upper and lower case)')
def c_user_type(file):
    '''Calculates the number of user based on their type'''
    try:
        counts=file['User Type'].value_counts()
        print('-'*20,'\nThe counts of each user type are ',counts)
    except:
        print('Something went wrong')

def gender_count(file):
    '''Computes the total of males in comparison to females when the gender is mentioned for the user'''
    try:
        counts=file['Gender'].value_counts()
        print('-'*20,'\nThe gender distribution is as following:',counts)
    except:
        print('Something went wrong')


def birth_years(file):
    '''Perform statistics for birth dates where highest computes the oldest birth date and the most recent birth date besides the highest year in birth date counts '''
    try:
        year=file['Birth Year']
        oldest=min(file['Birth Year'])
        youngest=max(file['Birth Year'])
        common=file['Birth Year'].mode()[0]
        print('-'*20,'\nThe youngest user was born in',youngest,'and the oldest user was born in',oldest,'\n',common,'is the most common birth year')
    except:
        print('Something went wrong')
while True:
    city = input("\nFor Washington press (W), for New York press (NY), for Chicago press (C), to exit press (s)\nYour choice is: ").lower()
    if city =='w':
        file=pd.read_csv(cities[city])
        print('\nYou have selected Washington')
        view_data(file)
        filter=input('\nDo you want to filter data by certain month or day? (y/n)').lower()
        if filter == 'y':
            filter_data(file)

        print('Please select the statistics you want to compute\n')
        try:
            sts=input('\nFor travel times statistics, press (1)\nFor stations and trips statistics, press (2)\nFor trip duration statistics, press (3)\n\nTo return to the main menu, press (S)\nYour Answer is: ')
        except:
            print('This is an unidentified letter')
        if sts=='1':
            #choose the type of sts to be calculated from the data
            tsts = input(
                '\n\nFor calculating the most common month, press (m)\nFor calculating the most popular day of week, press(d)\nFor calculating the most popular hour, press(h)\nFor returning to the main menu, press(s)\nYour Choice is: ')

            while True:
                tsts = input(
                    '\n\nFor calculating the most common month, press (m)\nFor calculating the most popular day of week, press(d)\nFor calculating the most popular hour, press(h)\nFor returning to the main menu, press(s)\nYour Choice is: ')

                if tsts=="m":
                    most_popular_month(file)
                    q = input('\nDo you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tsts=='d':
                    most_popular_day(file)
                    q = input('\nDo you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tsts=='h' :
                    most_popular_hour(file)
                    q = input('\nDo you want to compute another stat? (y/n)')
                    if q == 'n':
                        break

                elif tsts=='s':
                    break
                else:
                    print('An unidentified letter!!')
        elif sts=='2':
            while True:
                print('\nWhat is the type of statistics would you like to compute?')
                type=input('\nThe most common start station (1)\nThe most common end station (2)\nThe most common trip (3)\nTo return back, press (s)\nYour choice is: ')
                if type=='1':
                    most_ststaion(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif type=='2':
                    most_enstation(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif type=='3':
                    most_cotrip(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif type =='s':
                    break
                else:
                    print('Something is wrong')
        elif sts== '3':
            while True:
                tst=input('\nFor computing the total travel time, press (1)\nFor computing the average travel time, press (2),\nTo return back, press (s)\nYour answer: ')
                if tst == '1':
                    total_travel_time(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst =='2':
                    average_travel_time(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif type =='s':
                    break
                else:
                    print('Please enter either (1) or (2)')

    elif city=='c':
        file=pd.read_csv(cities[city])
        print('\nYou have selected Chicago\n')
        view_data(file)

        filter = input('\nDo you want to filter data by certain month or day? (y/n)').lower()
        if filter == 'y':
            filter_data(file)

        print('\nPlease select the statistics you want to compute')
        sts=input('\nFor travel times statistics, press (1)\nFor stations and trips statistics, press (2)\nFor trip duration statistics, press (3)\nFor User Info, press (4)\nTo return to the main menu, press (s)\nYour answer: ')
        if sts=='1':
            #choose the type of sts to be calculated from the data

            while True:
                tsts = input(
                    '\nFor calculating the most common month, press (m)\nFor calculating the most popular day of week, press(d)\nFor calculating the most popular hour, press(h)\nFor returning to the main menu, press(s). ')

                if tsts=="m":
                    most_popular_month(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tsts=='d':
                    most_popular_day(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tsts == 'h':
                    most_popular_hour(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tsts=='s':
                    break
                else:
                    print('\nSorry, this is an unidentfied letter')
        elif sts=='2':
            while True:
                print('\nWhat is the type of statistics would you like to compute?')
                type=input('\nThe most common start station (1)\nThe most common end station (2)\nThe most common trip (3)\nYour answer: ')
                if type=='1':
                    most_ststaion(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif type=='2':
                    most_enstation(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif type=='3':
                    most_cotrip(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                else:
                    print('Something is wrong')

        elif sts== '3':
            while True:
                tst=input('\nFor computing the total travel time, press (1)\nFor computing the average travel time, press (2),\nTo exit, press (3)\nYour answer: ')
                if tst == '1':
                    total_travel_time(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst =='2':
                    average_travel_time(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst  == '3':
                    break
                else:
                    print('Please enter either (1) or (2)')
        elif sts =='4':
            while True:
                tst = input(
                    '\nFor user types counts, press (1)\nFor the number of males and females, press (2)\nFor birth date statistics, press (3)\nYour answer: ')
                if tst == '1':
                    c_user_type(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst =='2':
                    gender_count(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst=='3':
                    birth_years(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                else:
                    print('Something went wrong')
        else:
            print('Sorry, something went wrong')



    elif city =='ny':
        file=pd.read_csv(cities['ny'])
        view_data(file)

        print('\nYou have selected New York City\n')
        filter = input('\nDo you want to filter data by certain month or day? (y/n)').lower()
        if filter == 'y':
            filter_data(file)
        print('Please select the statistics you want to compute\n')
        sts=input('\nFor travel times statistics, press (1)\nFor stations and trips statistics, press (2)\nFor trip duration statistics, press (3)\nFor User Info , press (4)\nTo exit the program, press (s).\nYour answer: ')
        if sts=='1':

            while True:
                tsts=input('\nFor calculating the most common month, press (m)\nFor calculating the most popular day of week, press(d)\nFor calculating the most popular hour, press(h)\nFor returning to the main menu, press(s).\nYour answer: ')
                if tsts=="m":
                    most_popular_month(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q=='n':
                        break
                elif tsts=='d':
                    most_popular_day(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q=='n':
                        break
                elif tsts=='h' :
                    most_popular_hour(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q=='n':
                        break
                elif tsts=='s':
                    break
                else:
                    print('Sorry, this is an unidentfied letter')
        elif sts=='2':
            while True:
                print('\nWhat is the type of statistics would you like to compute?')
                type=input('\nThe most common start station (1)\nThe most common end station (2)\nThe most common trip (3)\nYour answer: ')
                if type=='1':
                    most_ststaion(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif type=='2':
                    most_enstation(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif type=='3':
                    most_cotrip(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                else:
                    print('Something is wrong')
        elif sts== '3':
            while True:
                tst=input('\nFor computing the total travel time, press (1)\nFor computing the average travel time, press (2),\nTo exit, press (3)\nYour answer: ')
                if tst == '1':
                    total_travel_time(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst =='2':
                    average_travel_time(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst  == '3':
                    break
                else:
                    print('Please enter either (1) or (2)')
        elif sts == '4':
            while True:
                tst=input('\nFor user types counts, press (1)\nFor the number of males and females, press (2)\nFor birth date statistics, press (3)\nYour answer: ')
                if tst =='1':
                    c_user_type(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst =='2':
                    gender_count(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                elif tst=='3':
                    birth_years(file)
                    q = input('Do you want to compute another stat? (y/n)')
                    if q == 'n':
                        break
                else:
                    print('Something went wrong')
        else:
            print('Sorry, something went wrong')

    elif city =='s':
        break
        exit()
    else:
        print('This is an unidentified letter')

