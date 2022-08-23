import sys
import CEP_WA3_Student
import cepwa3cca

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
    (3) Update Student Offence List
    (4) Update Student's Badge List
    (5) Update Broken Items
    (6) Access Student Information 
    (7) Exit System''')

    inputnum = int(input("Pick an option: "))

    if inputnum == 1:
        print("Im here")
        myCCA.add_student(input("What is the name of your student: "))
        maincode()

    elif inputnum == 2:
        myCCA.remove_student()
        maincode()
    elif inputnum == 3:
        myCCA.update_offence_list()
        maincode()
    elif inputnum == 4:
        myCCA.update_badgelist()
        maincode()
    elif inputnum == 5:
        myCCA.update_bi()
        maincode()
    elif inputnum == 6:
        myCCA.access_student_info()
        maincode()
    elif inputnum == 7:
        sys.exit()

maincode()