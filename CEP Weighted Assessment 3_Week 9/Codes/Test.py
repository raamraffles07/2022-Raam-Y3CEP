import csv
from email import header

header = ["Name   ", "Class  ", "Register number  ", "Batch Number  ", "Number of Offences  ", "Number of Badges  ", "Number of Broken Items  ", "List of Offences  ", "List of Badges  ", "List of Broken Items  "]
header2 = ["Object   ", "Quantity   ", "Logistics Accessible   "]

with open("Dataset.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)

with open("LogisticsList.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(header2)
        