from CEP_WA3_Student import Student


class cca1:

    def add_student(self, name1):
        name1 = Student
        name1.offencelist = []
        name1.badgelist = []
        name1.brokenitems = []
        class1 = str(input("What is the Student's class: "))
        regnum1 = int(input("What is the Student's Register Number: "))
        batchnum1 = int(input("What is the Student's Batch Number: "))
        num_of_offences1 = int(input("What is the Student's Number of Offences: "))
        num_of_badges1 = int(input("What is the Student's Number of Badges: "))
        num_of_broken_items1 = int(input("What is the Student's Number of Broken items: "))
        name1.classs = class1
        name1.reg_num = regnum1
        name1.number_of_brokenitems = num_of_broken_items1
        for i in range(num_of_offences1):
            a = str(input("Date of Incident: "))
            b = str(input("Year of Incident: "))
            c = str(input("Description of Incident: "))
            name1.offencelist += [a, b, c]
        for i in range(num_of_badges1):
            a = str(input("Date of Badge Claim: "))
            b = str(input("Year of Incident: "))
            c = str(input("Name of Badge: "))
            name1.badgelist += [a, b, c]
        for i in range(num_of_broken_items1):
            a = str(input("Date of Broken Item: "))
            b = str(input("Year of Incident: "))
            c = str(input("Name of Broken Item: "))
            name1.brokenitems += [a, b, c]
        with open("Dataset.txt", "a") as f:
            f.write("Hi /n")
        
    def access_student_info():
        with open("Dataset.txt", "a") as f:
            f.write("new line\n")

    
        



        

        
        
        
     