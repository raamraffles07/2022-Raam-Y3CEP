import csv
from email import header

# These are the headers for the various files. 

header = ["Name   ", "Class  ", "Register number  ", "Batch Number  ", "Number of Offences  ", "Number of Badges  ", "Number of Broken Items  ", "List of Offences  ", "List of Badges  ", "List of Broken Items  ", "List of Absent Days  "]
header2 = ["Object   ", "Quantity   ", "Logistics Accessible   "]
header3 = ["Event Name   ", "Event Description   ", "Year   ", "Storage File Name   ", "Budget   ", "Total Budget Remaining   "]

def datasetheaderwriter(): 
    
    # This writes headers for dataset.csv

    with open("Dataset.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)

with open("LogisticsList.csv", "w") as f:

    # This writes headers for LogisticsList.csv

    writer = csv.writer(f)
    writer.writerow(header2)

def eventheaderwriter():

    # This writes headers for Events.csv

    with open("Events.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header3)

datasetheaderwriter()