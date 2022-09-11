from CEP_WA3_Student import Student
from CEP_WA3_Student import Event
import csv

class cca1:

    def add_student(self):

        """ 
        Takes student input from a student and writes the information into Dataset.csv.
        """

        # The following lines are just about obtaining user inputs, which can be used to create
        # a class in "Student".

        name3 = input('''
What is the name of the student: ''')

        class3 = str(input("What is the class of the student: "))
        regnum3 = str(input("What is the register number of the student: "))
        batchnum3 = str(input("What is the batch number of the student: "))
        numofoffences3 = int(input("What is the number of offences committed by the student: "))
        numofbadges3 = str(input("What is the number of badges earned by the student: "))
        numbrokeni3 = str(input("What is the number of items broken by the student: "))
        offencelist3 = ""
        badgelist3 = ""
        brokenilist3 = ""

        # The following for loops basically ensure that for every 1 badge a student has, the name of the badge,
        # and the date that it was claimed, is recorded. This also applies to, the offences he has committed, 
        # and the items he has broken. 

        for i in range(int(numofoffences3)):
            x = str(input("Enter name of offence: "))
            y1 = str(input("Enter the date of offence committed: "))
            y = y1[:2] + "/" + y1[2:4] + "/" + y1[4:]
            z = str(str(x) + " on " + y + ", ")
            offencelist3 += (z)
        for i in range(int(numofbadges3)):
            x = str(input("Enter name of badge: "))
            y1 = str(input("Enter the date of offence committed: "))
            y = y1[:2] + "/" + y1[2:4] + "/" + y1[4:]
            z = str(str(x) + " on " + y + ", ")
            badgelist3 += (z)
        for i in range(int(numbrokeni3)):
            x = str(input("Enter name of broken item: "))
            y1 = str(input("Enter the date of offence committed: "))
            y = y1[:2] + "/" + y1[2:4] + "/" + y1[4:]
            z = str(str(x) + " on " + y + ", ")
            brokenilist3 += (z)
        
        # This creates the "Student" class, to which specific attributes are provided as in the received input.

        name3 = Student(name3, class3, regnum3, batchnum3, numofoffences3, numofbadges3, numbrokeni3, offencelist3, badgelist3, brokenilist3)

        # This adds our "Student" class to our Dataset.csv.

        name3.addlist()

    def remove_student(self):

        """ 
        
        This function basically removes a student from the .csv file. 

        """

        # The following lines are just about obtaining user inputs, which can be used to remove a 
        # Student class from the program.

        name5 = str(input('''
    What is the name of the Student: '''))
        class3 = str(input('''
    What is the class of the Student: '''))
        regum3 = str(input('''
    What is the register number of the Student: '''))

        # This line retrieves our Dataset.csv

        lines = list(csv.reader(open('Dataset.csv')))

        for i in range(0, (len(lines))):
            ## Basically, if the name, class and register number provided as input to the code corresponds with a Student class
            ## in the .csv file, that particular row will be removed. 
            if (lines[i][0] == name5) and (lines[i][1] == class3) and (((lines[i][2])) == regum3):
                lines.remove(lines[i])
        
        # This line writes to our Dataset.csv, with the new appended information. 

        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)
    

    def update_offence_list(self):

        """ 
        
        This function is to update the offence list of students.

        """

        # This line retrieves our Dataset.csv
        
        r = csv.reader(open('Dataset.csv')) 

        # The following lines are similarly simply about obtaining user inputs.

        name4 = str(input('''
    What is the name of the Student: '''))
        r1 = str(input('''
    What is the offence committed by this student: '''))
        r2 = str(input('''
    What is the date of the offence: '''))
        r3 = str(r1 + " committed on " + r2[:2] + "/" + r2[2: 4] + "/" + r2[4:] + ", ")
        lines = list(r)
        class3 = str(input('''
    What is the class of the Student: '''))
        regum3 = str(input('''
    What is the register number of the Student: '''))

        for i in range(1, len(lines)):
            ## Basically, if the name, class and register number provided as input to the code corresponds with a Student class
            ## in the .csv file, the number of offences they have committed will increase by 1, and their offence list will also
            ## be added on to.
            if (lines[i][0] == name4) and (lines[i][1] == class3) and (((lines[i][2])) == regum3):
                y = int(int(lines[i][4]) + 1)
                lines[i][4] = y
                lines[i][7] += (r3)
        
        # These lines write to our Dataset.csv, with the new appended information. 
        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)


    def update_badgelist(self):

        ## This function is to update the badge list of students.
        ## The line below retrieves data from our dataset.

        r = csv.reader(open('Dataset.csv')) 

        # The following lines are similarly simply about obtaining user inputs.

        name4 = str(input('''
    What is the name of the Student: '''))
        r1 = ""
        x = int(input('''
    What is the name of badge earned: 
    (1) First Aid Knowledge
    (2) Youth Leadership
    (3) Service Learning
    (4) Red Cross Knowledge
    (5) Disaster Management
    (6) Footdrill

    '''))

        if x == 1:
            r1 += "First Aid Knowledge"
        elif x == 2:
            r1 += "Youth Leadership"
        elif x == 3:
            r1 += "Service Learning"
        elif x == 4:
            r1 += "Red Cross Knowledge"
        elif x == 5:
            r1 += "Disaster Management"
        else:
            r1 += "Footdrill"

        y = int(input('''
    What is the level of badge earned: 
    (1) Bronze
    (2) Silver
    (3) Gold
    
    '''))

        #Appending the "level" of badges to the specifics of badges in the file. 
        
        if y == 1:
            r1 += "(B)"
        elif y == 2:
            r1 += "(S)"
        elif y == 3:
            r1 += "(G)"

        r2 = str(input('''
    What is the date of the badge earned: '''))
        # Date at which badge is earned. 
        r3 = str(r1 + " earned on " + r2[:2] + "/" + r2[2: 4] + "/" + r2[4:] + ", ")

        lines = list(r)
        class3 = str(input('''
    What is the class of the Student: '''))
        regum3 = str(input('''
    What is the register number of the Student: '''))
        for i in range(1, len(lines)):
            if (lines[i][0] == name4) and (lines[i][1] == class3) and (((lines[i][2])) == regum3):

            ## Basically, if the name, class and register number provided as input to the code corresponds with a 
            ## Student class in the .csv file, the number of badges they have earned will increase by 1, and 
            ## their badge list will also be added on to, as well as the date of the badge claim.

                y = int(int(lines[i][5]) + 1)
                lines[i][5] = y
                lines[i][8] += (r3[:-2] + ", ")
        
        # These lines write to our Dataset.csv, with the new appended information. 

        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)


    def update_brokenitems(self):

    ## This function is to update the broken items list of students.

    ## The first part of the sub-function updates Dataset.csv, as in the record of students themselves.
    ## The line below retrieves data from the file, Dataset.csv.

        r = csv.reader(open('Dataset.csv')) 
        lines = list(r)
    
    ## Providing input as to the item that was broken. 

        t = int(input('''
    What is the item that was broken:
    (1) First Aid Kit
    (2) Roller Bandages
    (3) Triangular Bandages
    (4) Gauges
    (5) Saline Solution
    (6) Plasters
    (7) Fitness Training Kits

    '''))

        if t == 1:
            a = "First Aid Kit"
        elif t == 2:
            a = "Roller Bandages"
        elif t == 3:
            a = "Triangular Bandages"
        elif t == 4:
            a = "Gauges"
        elif t == 5:
            a = "Saline Solution"
        elif t == 7:
            a = "Fitness Training Kits"
        else:
            a = "Plasters"
    
    # Other similar particulars of the broken items, as well as the Student who broke them.

        b = int(input('''
    What is the number of items that got broken: '''))
        c = str(input('''
    What is the name of the student that broke the item: '''))
        d = str(input('''
    What is the date at which the item was broken: '''))
        r3 = str(str(b) + " " + a + " broken on " + d[:2] + "/" + d[2: 4] + "/" + d[4:] + ", ")
        class3 = str(input('''
    What is the class of the Student: '''))
        regum3 = str(input('''
    What is the register number of the Student: '''))

    # If a student with a name in c is recognised in the system, with a register number as in regum3 and 
    # a class as in class3, the offence will be appended to his list of offences. That is the function of the
    # lines below.

        for i in range(1, len(lines)):
            if (lines[i][0] == c) and (lines[i][1] == class3) and (((lines[i][2])) == regum3):
                y = int(int(lines[i][6]) + b)
                lines[i][6] = y
                lines[i][9] += (r3[:-2] + ", ")
        
    # These lines write to our Dataset.csv, with the new appended information. 

        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)

    ## The second part of the sub-function updates LogisticsList.csv, as when an item is broken by a student, the 
    ## logistics list will be affected. The line below obtains the data from LogisticsList.csv.
    ## Basically, the number of items available of a particular Logistics item will be reduced by 1. 

        s = csv.reader(open('LogisticsList.csv')) 
        lines3 = list(s)
        for i in range(len(lines3)):
            if lines3[i][0] == str(a + "   "):
                lines3[i][2] = int(int(lines3[i][2]) - b)
        
    # These lines write to our LogisticsList.csv, with the new appended information. 
        writer = csv.writer(open('LogisticsList.csv', 'w'))
        writer.writerows(lines3)
        

        
    def access_student_info(self):

    ## This function is quite simple and self-explanatory. It basically returns the badge list/offence list/number of 
    ## broken items by students. The line below obtains the data from Dataset.csv.

        r = csv.reader(open('Dataset.csv')) 
        lines = list(r)
    
    ## Readers input what kind of information they want to access. 

        c = int(input('''

    Which of the following information would you like to access?

    (1) Student Badge List
    (2) Student Offence List
    (3) Student number of Broken Items
    
    '''))

    ## This function is quite simple and self-explanatory. If one wants to access this particular attribute of a student, 
    ## assuming that the name of this student, the student's class and the student's register number corresponds with a 
    ## Student class in Dataset.csv, this particular attribute of the student will be returned.

        if c == 1:
            a = 8
            b = str(input('''
    What is the name of the Student: '''))
            b34567 = str(input('''
    What is the batch number of the Student: '''))
            for i in range(1, len(lines)):
                if (lines[i][0] == b) and (lines[i][3] == b34567):
                    print('''
 BADGES EARNED BY STUDENT:
            ''')
                    a1 = (lines[i][8]).split(", ")
                    for i in a1:
                        print(" " + i)

    ## This function is quite simple and self-explanatory. If one wants to access this particular attribute of a student, 
    ## assuming that the name of this student, the student's class and the student's register number corresponds with a 
    ## Student class in Dataset.csv, this particular attribute of the student will be returned.

        if c == 2:
            a = 7
            b = str(input('''
    What is the name of the Student: '''))
            b34567 = str(input('''
    What is the batch number of the Student: '''))
            for i in range(1, len(lines)):
                if (lines[i][0] == b) and (lines[i][3] == b34567):
                    print('''
 The offences committed by the Student:
            ''')
                    d = (lines[i][a][: -2]).split(", ")
                    for i in d:
                        print(" --> " + i)
    
    ## This function is quite simple and self-explanatory. If one wants to access this particular attribute of a student, 
    ## assuming that the name of this student, the student's class and the student's register number corresponds with a 
    ## Student class in Dataset.csv, this particular attribute of the student will be returned.

        if c == 3:
            a = 9
            b = str(input('''
    What is the name of the Student: '''))
            b34567 = str(input('''
    What is the batch number of the Student: '''))
            for i in range(1, len(lines)):
                if (lines[i][0] == b) and (lines[i][3] == b34567):
                    print('''
 The items broken by the student:
            ''')
                    d = (lines[i][a][: -2]).split(", ")
                    for i in d:
                        print(i)
    
    def access_logistics_info(self):

    ## This function is quite simple and self-explanatory. It basically returns the logistics list available.
    ## The line below accesses the data in LogisticsList.csv.

        r = csv.reader(open('LogisticsList.csv')) 
        lines = list(r)
        print('''
    ''')
        for i in range(1, (len(lines) - 1)):
            print(str(lines[i][0]) + "--> Total Number: " + (str(lines[i][1]))[:3] + ", Total available: " + str(lines[i][2]))
            print('''
    ''')
    
        
    def update_events_info(self):

    ## Another aim of my code is to keep in track the important events that goes on in my CCA. Right now, there are about 200 
    ## different folders within the common 'events' folder, and it is very hard to access information. This basically solves 
    ## that problem with a single common folder where information can be easily accessed. 
        

        #The following is a series of user inputs. 

        desc_name = str(input('''
    
    What is the name of the event: 
    '''))

        desc3 = str(input('''
    Enter the description of the event here:
    '''))

        desc_date = (str(input('''
    What is the date that this event happened: 
    ''')))

        desc_year = desc_date[:2] + "/" + desc_date[2:4] + "/" + desc_date[4:]

        desc_file1 = str(input('''
    What is the name of the file with the event particulars: 
    '''))
        desc_cost = int(input('''
    What is the budget of the event: '''))

        # The lines below create an "Event" class, which is appended to "Events_2022.csv" via the function 
        # desc_name.addlist_events().

        desc_name = Event(desc_name, desc3, desc_year, desc_file1, desc_cost)

        desc_name.addlist_events()
    

    def access_events_info(self):

    ## This function is quite simple and self-explanatory. It basically returns the particulars of the event the 
    ## user has asked for. The line below access the data in LogisticsList.csv.
    
        r = list(csv.reader(open('Events_2022.csv')))[1:]
        ## The line below retrieves information in Events_2022.csv.

        a = str(input('''
    What is the name of the event:  
    '''))
        for i in r:
            if i[0] == a:

                
                ## If the name of the Event the user has entered exists in Events_2022.csv, then the particulars of 
                ## the event will be returned, as shown below. 
                
                print('''
    The name of the event is ''' + str(i[0]) + ".")
                print('''
    Here is the descriptions of the event:
    
    ''' + str(i[1]))
                print('''
    The event happened in ''' + str(i[2]) + ".")
                print('''
    More information regarding the event can be found in the file: ''' + str(i[3]))
                print('''
    The total amount of money spent on the event is: $''' + str(i[4]))
                print('''
    The total amount of budget remaining after the event is: $''' + str(i[5]))
    
    def update_attendee_list(self):

        ## A series of user input about the student whose attendance needs to be updated is below.

        b = str(input('''
    What is the name of the Student: '''))
        c = str(input('''
    What is the class of the Student: '''))
        d = str(input('''
    What is the register number of the Student: '''))
        e = str(input(''' 
    What is the date that the Student was absent on: '''))
        e2 = e[:2] + "/" + e[2:4] + "/" + e[4:]
        f = str(input(''' 
    What is the reason for the Student's Absence: '''))

        # The information in Dataset.csv is retrieved.

        r = list(csv.reader(open('Dataset.csv')))

        for i in r:

            # If the Student name, Student class and Student register number correspond with a Student class in 
            # Student class in Dataset.csv, the Student's attendance list will be updated. 

            if (i[0] == b) and (i[1] == c) and (i[2] == d):
                i[10] += str("Absent on: " + e2 + " due to " + f + ".")
        
        # These lines write to our Dataset.csv, with the new appended information. 
        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(r)
    
    def access_attendee_list(self):

        # User inputs

        b = str(input('''
    What is the name of the Student: '''))
        c = str(input('''
    What is the class of the Student: '''))
        d = str(input('''
    What is the register number of the Student: '''))

        # Retrieving information in Dataset.csv
        r = list(csv.reader(open('Dataset.csv')))

        # Assuming that a particular Student class exists as per the user's input, 
        # the student's attendance, or rather, the days he were absent, is returned. 
        
        for i in r:
            if (i[0] == b) and (i[1] == c) and (i[2] == d):
                a = i[10].split(".")
                print('''
    ''')
                for i in a:
                    print(i)
                    print('''
    ''')