import csv
from csv import writer
from Test import datasetheaderwriter
from operator import itemgetter

class Student:

    def __init__(self, name, classs, regnum, batchnum, numoffences, numbadges, numbrokeni, offencelist = "", badgelist = "", brokenilist = ""):
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
    
    def addlist(self):
        with open("Dataset.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Class", "Register number", "Batch Number", "Number of Offences", "Number of Badges", "Number of Broken Items", "List of Offences", "List of Badges", "List of Broken Items"])
            writer.writerow({"Name": self.name, "Class": self.classs, "Register number": self.regum, "Batch Number": self.batchnum, "Number of Offences": self.numoffences, "Number of Badges": self.numbadges, "Number of Broken Items": self.numbrokeni, "List of Offences": self.offencelist, "List of Badges": self.badgelist, "List of Broken Items": self.brokenilist})
        
        r = list(csv.reader(open('Dataset.csv')))
        r3 =  sorted((r[1:]), key=itemgetter(3))
        writer = csv.writer(open('Dataset.csv', 'w'))
        writer.writerows(r3)

    
class Event:

    def __init__(self, desc_name, desc3, desc_year, desc_file1, desc_cost, y = 0):
        self.desc_name = desc_name
        self.description = desc3
        self.year = desc_year
        self.file1 = desc_file1
        self.cost = desc_cost
        self.remaining = y
    
    def addlist_events(self):

        ## Append to Events.csv

        with open("Events.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Event Name", "Event Description", "Year", "Storage File Name", "Budget", "Total Budget Remaining"])
            writer.writerow({"Event Name": self.desc_name, "Event Description": self.description, "Year": self.year, "Storage File Name": self.file1, "Budget": self.cost, "Total Budget Remaining": self.remaining})
