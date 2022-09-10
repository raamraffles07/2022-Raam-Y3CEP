import sys
import CEP_WA3_Student
import cepwa3cca
import csv

myCCA = cepwa3cca.cca1()

def maincode():

    print('''
    This is RIRC's Record Tracking System!!! 
    Here, you can access all of your students' information, 
    as well as information regarding logisticts and events. 
    Hope you Enjoy using this program!
    ''')

    print('''

    Firstly, before running the program, please remember to reverse changes to 
    both the files: LogsticsList.csv and Dataset.csv, just in case their data have been erased!

    Please make choose one of the following 7 choices:
    (1) Add Student 
    (2) Remove Student
    (3) Update Student information
    (4) Update Important Events information
    (5) Access Student Info
    (6) Access Logistics Info
    (7) Access Events information
    (8) Update Attendee List
    (9) Access Attendee List
    (10) Exit System''')

    ## Setting inputnum to be 0 for the 'while loop' to function.
    inputnum = 0

    while (((inputnum > 0) == False) or ((inputnum < 11) == False)):
        
        try:
            inputnum = int(input('''
    
    Pick an option: '''))

        ## Here is one of the try-except commands

        except ValueError:
            
            inputnum = int(input('''
        
    Sorry, please input an integer for the system to function: '''))

    ## Here is where the sub-functions of my program are called. 

    if inputnum == 1:
        myCCA.add_student() #Add student function
        maincode()
    
    elif inputnum == 2:
        myCCA.remove_student() #Remove student function
        maincode()

    elif inputnum == 3:

        x = int(input('''

    Pick an Option:
    (1) Update Student Offence List
    (2) Update Student Badge List
    (3) Update Student Broken Items List

    ''')) 

    #This above, is asking for a another input to decide on which of the 3 functions below to use.
    # Whether to update offence list, badge list, or broken items list. 

        if x == 1:
            myCCA.update_offence_list()
            maincode()

        elif x == 2:
            myCCA.update_badgelist()
            maincode()

        elif x == 3:
            myCCA.update_brokenitems()
            maincode()
    
    # Other functions of my program below 
    
    elif inputnum == 4:
        myCCA.update_events_info()
        maincode()

    elif inputnum == 5:
        myCCA.access_student_info()
        maincode()
    
    elif inputnum == 6:
        myCCA.access_logistics_info()
        maincode()
    
    elif inputnum == 7:
        myCCA.access_events_info()
        maincode()
    
    elif inputnum == 8:
        myCCA.update_attendee_list()
        maincode()
    
    elif inputnum == 9:
        myCCA.access_attendee_list()
        maincode()

    elif inputnum == 10:
        ## Exit System
        sys.exit()

maincode()
