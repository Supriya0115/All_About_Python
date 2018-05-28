# Code for PyBank

"""
A function BankSummary has been defined to take an input csv file, and return an output text file. The input file contains Revenue Data. 
The output file aggregates the Revenue Data and provides meaningful summary.

"""

def BankSummary(InputFile,OutputFile):

    # Import packages

    import os   
    import csv
    from datetime import date

    # Define the csv path

    cvs_path = os.path.join('../','Resources',InputFile)

    #Initialize variables

    Total = 0
    Month = 0
    Revenue = []
    Month_1 = []
    Revenue_Change = []
    

    # Read csv and create file object

    with open(cvs_path, newline = '') as BFile:
        Budget_Data = csv.reader(BFile,delimiter = ',')
        next(Budget_Data, None)

    # Read each row and extract Revenue and Month to lists, calculate Total Revenue and Months

        for row in Budget_Data:
            Total = Total + int(row[1])
            Month = Month + 1
            Revenue.append(int(row[1]))
            Month_1.append(row[0])
            
    # Calculate month on month revenue change and store it in a list Revenue_Change

        Revenue_Change.append(Revenue[0])

        for x in range(1,len(Revenue)):
            Revenue_Change.append(Revenue[x]-Revenue[x-1])

    # Determine greatest increase and decrease in revenue
 
        Max_Revenue_Change = max(Revenue_Change)
        Min_Revenue_Change = min(Revenue_Change)
        Average_Revenue_Change = round(sum(Revenue_Change)/len(Revenue_Change))

    # Zip revenue change and month and convert to dictionary. This is to determine the month 
    # associated with greatest increase/decrease in revenue

        Stock_Dictionary = dict(zip(Month_1,Revenue_Change))

        for key, value in Stock_Dictionary.items():
            if value == Max_Revenue_Change:
                Month_Max_Revenue_Change = key
            if value == Min_Revenue_Change:
                Month_Min_Revenue_Change = key


    # Append Run Date to File Name for easier identification of files

        File_Name = (OutputFile + "_" + str(date.today()) + ".txt")

        with open(File_Name,'w') as BankSummary:

    # Print the output to a text file

            BankSummary.write("Financial Analysis\n")
            BankSummary.write("-"*30 + "\n")
            BankSummary.write("Total Months: " + str(Month) + "\n")
            BankSummary.write("Average Revenue Change: " + "$" + str(Average_Revenue_Change) + "\n")
            BankSummary.write("Greatest Increase in Revenue: " + Month_Max_Revenue_Change + " (" + "$" + str(Max_Revenue_Change) + ")" + "\n")
            BankSummary.write("Greatest Decrease in Revenue: " + Month_Min_Revenue_Change + " (" + "$" + str(Min_Revenue_Change) + ")" + "\n")

    # Print the output to the terminal

            print("Financial Analysis")
            print("-"*30)
            print("Total Months: " + str(Month))
            print("Average Revenue Change: " + "$" + str(Average_Revenue_Change))
            print("Greatest Increase in Revenue: " + Month_Max_Revenue_Change + " (" + "$" + str(Max_Revenue_Change) + ")")
            print("Greatest Decrease in Revenue: " + Month_Min_Revenue_Change + " (" + "$" + str(Min_Revenue_Change) + ")")



# Call BankSummary function with necessary arguments

BankSummary('budget_data_1.csv','BankSummary1')

BankSummary('budget_data_2.csv','BankSummary2')
