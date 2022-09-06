from CEP_WA3_Student import Student
from CEP_WA3_Student import Event
import csv

class cca1:

    def add_student(self):
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
        for i in range(int(numofoffences3)):
            x = str(input("Enter name of offence: "))
            y = str(input("Enter the date of offence committed: "))
            z = str(str(x) + " on " + y)
            offencelist3 += (z)
        for i in range(int(numofbadges3)):
            x = str(input("Enter name of badge: "))
            y = str(input("Enter the date of badge earned: "))
            z = str(str(x) + " on " + y)
            badgelist3 += (z)
        for i in range(int(numbrokeni3)):
            x = str(input("Enter name of broken item: "))
            y = str(input("Enter the date of item broken: "))
            z = str(str(x) + " on " + y)
            brokenilist3 += (z)
        name3 = Student(name3, class3, regnum3, batchnum3, numofoffences3, numofbadges3, numbrokeni3, offencelist3, badgelist3, brokenilist3)
        name3.addlist()


    def remove_student(self):
        name5 = str(input("What is the name of the Student: "))
        r = csv.reader(open('Dataset.csv')) 
        lines = list(r)
        for i in range(1, (len(lines) - 1)):
            if lines[i][0] == name5:
                lines = lines[:i] + lines[(i + 1):]
        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)
    

    def update_offence_list(self):
        r = csv.reader(open('Dataset.csv')) 
        name4 = str(input('''
    What is the name of the Student: '''))
        r1 = str(input('''
    What is the offence committed by this student: '''))
        r2 = str(input('''
    What is the date of the offence: '''))
        r3 = str(r1 + " committed on " + r2[:2] + "/" + r2[2: 4] + "/" + r2[4:] + ", ")
        lines = list(r)
        for i in range(1, len(lines)):
            if lines[i][0] == name4:
                y = int(int(lines[i][4]) + 1)
                lines[i][4] = y
                lines[i][7] += (r3)
        writer = csv.writer(open('Dataset.csv', 'w'))

        writer.writerows(lines)


    def update_badgelist(self):

        r = csv.reader(open('Dataset.csv')) 
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

        if y == 1:
            r1 += "(B)"
        elif y == 2:
            r1 += "(S)"
        elif y == 3:
            r1 += "(G)"

        r2 = str(input('''
    What is the date of the badge earned: '''))
        r3 = str(r1 + " earned on " + r2[:2] + "/" + r2[2: 4] + "/" + r2[4:] + ", ")

        lines = list(r)

        for i in range(1, len(lines)):
            if lines[i][0] == name4:
                y = int(int(lines[i][5]) + 1)
                lines[i][5] = y
                lines[i][8] += (r3[:-2] + ", ")

        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)


    def update_brokenitems(self):
    
    ## Update Dataset.csv

        r = csv.reader(open('Dataset.csv')) 
        lines = list(r)

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

        b = int(input('''
    What is the number of items that got broken: '''))
        c = str(input('''
    What is the name of the student that broke the item: '''))
        d = str(input('''
    What is the date at which the item was broken: '''))
        r3 = str(str(b) + " " + a + " broken on " + d[:2] + "/" + d[2: 4] + "/" + d[4:] + ", ")


        for i in range(1, len(lines)):
            if lines[i][0] == c:
                y = int(int(lines[i][6]) + b)
                lines[i][6] = y
                lines[i][9] += (r3[:-2] + ", ")

        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)

    ## Update LogisticsList.csv

        s = csv.reader(open('LogisticsList.csv')) 
        lines3 = list(s)
        print(lines3)
        for i in range(1,8):
            if lines3[i][0] == str(a + "   "):
                lines3[i][2] = int(int(lines3[i][2]) - b)

        writer = csv.writer(open('LogisticsList.csv', 'w'))
        writer.writerows(lines3)
        

        
    def access_student_info(self):
        r = csv.reader(open('Dataset.csv')) 
        lines = list(r)
        c = int(input('''

    Which of the following information would you like to access?
    (1) Student Badge List
    (2) Student Offence List
    (3) Student number of Broken Items
    
    '''))

        if c == 1:
            a = 8
            b = str(input('''
    What is the name of the Student: '''))
            for i in range(1, len(lines)):
                if lines[i][0] == b:
                    print('''
 BADGES EARNED BY STUDENT:
            ''')
                    a1 = (lines[i][8]).split(", ")
                    for i in a1:
                        print(" " + i)

        if c == 2:
            a = 7
            b = str(input('''
    What is the name of the Student: '''))
            for i in range(1, len(lines)):
                if lines[i][0] == b:
                    print('''
 The offences committed by the Student:
            ''')
                    d = (lines[i][a][: -2]).split(", ")
                    print(d)

        if c == 3:
            a = 9
            b = str(input('''
    What is the name of the Student: '''))
            for i in range(1, len(lines)):
                if lines[i][0] == b:
                    print('''
 The items broken by the student:
            ''')
                    d = (lines[i][a][: -2]).split(", ")
                    print(d)
    
    def access_logistics_info(self):

        r = csv.reader(open('LogisticsList.csv')) 
        lines = list(r)
        for i in range(1, (len(lines) - 1)):
            print(lines[i])
    
        
    def update_events_info(self):
        
        desc_name = str(input('''
    
    What is the name of the event: 
    '''))
        desc3 = str(input('''
    Enter the description of the event here:
    '''))
        desc_year = int(input('''
    What is the year that this event happened: 
    '''))
        desc_file1 = str(input('''
    What is the name of the file with the event particulars: 
    '''))
        desc_cost = int(input('''
    What is the budget of the event: '''))

        desc_name = Event(desc_name, desc3, desc_year, desc_file1, desc_cost)

        desc_name.addlist_events()

        ## Append Last Element 
        
         



        

        
        
        
     