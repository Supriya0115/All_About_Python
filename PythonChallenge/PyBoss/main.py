# Code for PyBoss

"""
A function EmployeeData has been defined to take an input csv file, and return an output csv file. The input file contains employee records. 
The output file reformats the employee data - Name, DOB, State.

"""

def EmployeeData(InputFile,OutputFile):

    # Import packages

    import os

    import csv

    # Define the csv path

    EmployeeCSV_1 = os.path.join("../", "Resources", InputFile)

    # Define empty list to hold reformatted employee data

    new_employee_data = []

    # Dictionary for US States and Codes, adapted from https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }


    # Open the input file, and reads it to a dictionary object. For every row in input csv -
    # Name is split to First Name, Last Name; First 5 digits of SSN are masked; State is transformed to letter code

    with open(EmployeeCSV_1) as reader:
        EmployeeCSV = csv.DictReader(reader)
        next(EmployeeCSV, None)
        for row in EmployeeCSV:
            First_Name = row["Name"].split(" ")[0]
            Last_Name = row["Name"].split(" ")[1]
            SSN_Last4 = row["SSN"][-4:]
            SSN_First5 = f"***-**-"
            SSN_Masked = f"{SSN_First5}{SSN_Last4}"

            for key, value in us_state_abbrev.items():
                if row["State"] == key:
                    State = value
    
    # Append the formatted data set to the empty list new_employee_data
    
            new_employee_data.append(
                {
                    "EMP ID": row["Emp ID"],
                    "First Name": First_Name,
                    "Last Name":  Last_Name,
                    "DOB": row["DOB"],
                    "SSN": SSN_Masked,
                    "State": State
                }
            )          

    # Define the output file path, write the data set to the output

        # EmployeeCSV_2 = os.path.join("..", "Resources", OutputFile)

        EmployeeCSV_2 = os.path.join(OutputFile)

        with open(EmployeeCSV_2,"w",newline = '') as csvfile:
            writer_fieldnames = ["EMP ID","First Name","Last Name","DOB","SSN","State"]
            EmployeeCSV = csv.DictWriter(csvfile, fieldnames = writer_fieldnames)
            EmployeeCSV.writeheader()
            EmployeeCSV.writerows(new_employee_data)

# Call BankSummary function with necessary arguments

EmployeeData('employee_data1.csv','Employee_Data_File1.csv')

EmployeeData('employee_data2.csv','Employee_Data_File2.csv')
