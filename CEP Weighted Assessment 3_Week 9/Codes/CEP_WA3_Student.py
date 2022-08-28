import csv
from csv import writer

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

