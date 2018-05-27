import os

import csv

EmployeeCSV_1 = os.path.join("..", "Resources", "employee_data1.csv")

new_employee_data = []

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

    EmployeeCSV_2 = os.path.join("..", "Resources", "Employee.csv")
    with open(EmployeeCSV_2,"w",newline = '') as csvfile:
        writer_fieldnames = ["EMP ID","First Name","Last Name","DOB","SSN","State"]
        EmployeeCSV = csv.DictWriter(csvfile, fieldnames = writer_fieldnames)
        EmployeeCSV.writeheader()
        EmployeeCSV.writerows(new_employee_data)

