import csv
from csv import writer
from Test import datasetheaderwriter
from operator import itemgetter

class Student:

    # This creates a 'Student' class and gives it attributes of a student. These attributes will be added to the 
    # Dataset.csv file later on. 

    def __init__(self, name, classs, regnum, batchnum, numoffences, numbadges, numbrokeni, offencelist = "", badgelist = "", brokenilist = "", absenteelist = ""):
        self.name = name
        self.classs = classs
        self.regum = regnum
        self.batchnum = batchnum
        self.numoffences = numoffences
        self.numbadges = numbadges
        self.numbrokeni = numbrokeni
        self.offencelist = offencelist
        self.badgelist = badgelist
        self.brokenilist = brokenilist
        self.absenteelist = absenteelist

    def addlist(self):

        # This adds an object 'Student' into the file Dataset.csv. This was basically written using 
        # Python_File_IO.pdf.

        with open("Dataset.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Class", "Register number", "Batch Number", "Number of Offences", "Number of Badges", "Number of Broken Items", "List of Offences", "List of Badges", "List of Broken Items", "List of Absent Days"])
            writer.writerow({"Name": self.name, "Class": self.classs, "Register number": self.regum, "Batch Number": self.batchnum, "Number of Offences": self.numoffences, "Number of Badges": self.numbadges, "Number of Broken Items": self.numbrokeni, "List of Offences": self.offencelist, "List of Badges": self.badgelist, "List of Broken Items": self.brokenilist, "List of Absent Days": self.absenteelist})
    

    
class Event:

    def __init__(self, desc_name, desc3, desc_year, desc_file1, desc_cost, y = 0):

    # This creates a 'Events' class and gives it attributes of an Event. These attributes will be added to the 
    # Events.csv file later on. 

        self.desc_name = desc_name
        self.description = desc3
        self.year = desc_year
        self.file1 = desc_file1
        self.cost = desc_cost
        self.remaining = y
    
    def addlist_events(self):

        # This adds an object 'Event' into the file Events_2022.csv. This was also basically written using 
        # Python_File_IO.pdf
        
        with open("Events_2022.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Event Name", "Event Description", "Year", "Storage File Name", "Budget", "Total Budget Remaining"])
            writer.writerow({"Event Name": self.desc_name, "Event Description": self.description, "Year": self.year, "Storage File Name": self.file1, "Budget": self.cost, "Total Budget Remaining": self.remaining})


        # The following 3 lines of code update the remaining budget of our CCA. Although the mathematical skills of 
        # many RI students is quite remarkable, it is very very tedious, especially when calculating remaining budgets 
        # with over 20 different events.

        r = list(csv.reader(open('Events_2022.csv')))
        r[-1][-1] = float(float(r[-2][-1]) - float(r[-1][-2]))
        writer = csv.writer(open('Events_2022.csv', 'w'))
        writer.writerows(r)
        