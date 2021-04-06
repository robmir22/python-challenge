import os
import csv

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

csvpath = os.path.join("Resources", "employee_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    Emp_id  = []
    Complete_name = []
    DOB = []
    socialsec = []
    State = []

    FirstName = []
    SecondName = []
    SocialModified = []

    for row in csvreader:
        Emp_id.append(row[0])
        Complete_name.append(row[1])
        DOB.append(row[2])
        socialsec.append(row[3])
        State.append(us_state_abbrev[row[4]])

for name in Complete_name:
    a = (name.split(" "))
    FirstName.append(a[0])
    SecondName.append(a[1])

for number in socialsec:
    var = number[-4:]
    SocialModified.append(f'***-**-{var}')

#1957-12-20 YYYY-MM-DD
#12/20/1957 MM/DD/YYYY
year = []
month = []
day = []
newDOB = []

for date in DOB:
    info = date.split("-")
    year.append(info[0])
    month.append(info[1])
    day.append(info[2])

newDOB = zip(month,day,year)
newnewDOB = [str(x)+"/"+str(y)+"/"+str(z) for (x,y,z) in newDOB]



output_path = os.path.join( "analysis", "Employee_list.csv")

final = zip(Emp_id, FirstName, SecondName,newnewDOB, SocialModified, State)


with open(output_path, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    writer.writerows(final)