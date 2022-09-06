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
    Please make choose one of the following 7 choices:
    (1) Add Student 
    (2) Remove Student
    (3) Update Student information
    (4) Update Important Events information
    (5) Access Student Info
    (6) Access Logistics Info
    (7) Access Events information
    (8) Exit System''')

    inputnum = int(input('''
    
    Pick an option: '''))

    if inputnum == 1:
        myCCA.add_student()
        maincode()
    
    elif inputnum == 2:
        myCCA.remove_student()
        maincode()

    elif inputnum == 3:

        x = int(input('''
    Pick an Option:
    (1) Update Student Offence List
    (2) Update Student Badge List
    (3) Update Student Broken Items List

    '''))

        if x == 1:
            myCCA.update_offence_list()
            maincode()

        elif x == 2:
            myCCA.update_badgelist()
            maincode()

        elif x == 3:
            myCCA.update_brokenitems()
            maincode()
    
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
        sys.exit()

maincode()