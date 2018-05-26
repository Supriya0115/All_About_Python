# Code for PyBank

# Import packages
import os
import csv

# Define the csv path
cvs_path = os.path.join('../../..','Resources','budget_data_1.csv')

#Initialize variables
Total = 0
Month = 0
Revenue_Change = [0]

# Read csv and create file object
with open(cvs_path, newline = '') as BFile:
    Budget_Data = csv.reader(BFile,delimiter = ',')
    next(Budget_Data, None)

    for row in Budget_Data:
        Revenue_Change.append(int(row[1])-Revenue_Change[-1])
        Total = Total + int(row[1])
        Month = Month + 1

    Max_Revenue_Change = row[Revenue_Change.index(max(Revenue_Change))]

    Min_Revenue_Change = row[Revenue_Change.index(min(Revenue_Change))]

    print(Max_Revenue_Change)