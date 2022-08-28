from CEP_WA3_Student import Student
import csv

class cca1:

    def add_student(self):
        name3 = str(input("What is the name of the student: "))
        class3 = str(input("What is the class of the student: "))
        regnum3 = str(input("What is the register number of the student: "))
        batchnum3 = str(input("What is the batch number of the student: "))
        numofoffences3 = int(input("What is the number of offences committed by the student: "))
        numofbadges3 = str(input("What is the number of badges earned by the student: "))
        numbrokeni3 = str(input("What is the number of items broken by the student: "))
        offencelist3 = []
        badgelist3 = []
        brokenilist3 = []
        for i in range(int(numofoffences3)):
            x = str(input("Enter name of offence: "))
            y = str(input("Enter the date of offence committed: "))
            z = str(str(x) + " on " + y)
            offencelist3.append(z)
        for i in range(int(numofbadges3)):
            x = str(input("Enter name of badge: "))
            y = str(input("Enter the date of badge earned: "))
            z = str(str(x) + " on " + y)
            badgelist3.append(z)
        for i in range(int(numbrokeni3)):
            x = str(input("Enter name of broken item: "))
            y = str(input("Enter the date of item broken: "))
            z = str(str(x) + " on " + y)
            brokenilist3.append(z)
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
        name4 = str(input("What is the name of the Student: "))
        r1 = str(input("What is the offence committed by this student: "))
        r2 = str(input("What is the date of the offence: "))
        r3 = str(r1 + " committed on " + r2 + ", ")
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
        name4 = str(input("What is the name of the Student: "))
        r1 = str(input("What is the name of badge earned: "))
        r2 = str(input("What is the date of the badge earned: "))
        r3 = str(r1 + " earned on " + r2 + ", ")

        lines = list(r)

        for i in range(1, len(lines)):
            if lines[i][0] == name4:
                y = int(int(lines[i][5]) + 1)
                lines[i][5] = y
                lines[i][8] += (r3[:-2] + ", ")

        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)


    def update_brokenitems(self):

        r = csv.reader(open('Dataset.csv')) 
        lines = list(r)

        a = str(input("What is the name of the student that broke the item: "))
        b = int(input("What is the number of items that got broken: "))
        c = str(input("What is the item that got broken: "))
        d = str(input("What is the date at which the item was broken: "))
        r3 = str(c + " broken on " + d + ", ")


        for i in range(1, len(lines)):
            if lines[i][0] == a:
                y = int(int(lines[i][6]) + b)
                lines[i][6] = y
                lines[i][9] += (r3[:-2] + ", ")

        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(lines)

        
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
            b = str(input("What is the name of the Student: "))
            for i in range(1, len(lines)):
                if lines[i][0] == b:
                    print("The badges earned by the Student: " + lines[i][a][: -2])
        if c == 2:
            a = 7
            b = str(input("What is the name of the Student: "))
            for i in range(1, len(lines)):
                if lines[i][0] == b:
                    print("The offences committed by the Student: " + lines[i][a][: -2])
        if c == 3:
            a = 9
            b = str(input("What is the name of the Student: "))
            for i in range(1, len(lines)):
                if lines[i][0] == b:
                    print("The items broken by the student: " + lines[i][a][: -2])
    
    def access_logistics_info(self):
        r = csv.reader(open('LogisticsList.csv')) 
        lines = list(r)
        for i in range(1, (len(lines) - 1)):
            print(lines[i])
    
        



        

        
        
        
     