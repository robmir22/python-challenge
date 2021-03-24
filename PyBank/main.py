#The dataset is composed of two columns: Date and Profit/Losses. #
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)


#Data is similar to a dictionary
#
#Import file CSV to read
#
#Jan 2010 change will be empty
#
#Element 1 - Element 0 will be new element change
#and assign to month FEB 10 as dictionary

# -------------------------------------------------

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
#with open(csvpath) as csvfile:
#    csvreader = csv.reader(csvfile, delimiter=",")
#    csv_header = next(csvreader)
#    month_count = 0
#    total = 0
#    for row in csvreader:
#        month_count += 1
#        total += int(row[1])
#    print(month_count)
#    print(total)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    monthly_changes1 = [int(row[1]) for row in csvreader]
    
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    next(csvreader)   
    monthly_changes2 = [int(row[1]) for row in csvreader]
    month_change = [row[0] for row in csvreader]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    next(csvreader)   
    month_change = [row[0] for row in csvreader]

monthly_changes1.pop(85)

print(monthly_changes1)
print(monthly_changes2)
print(month_change)

print(len(monthly_changes1))
print(len(monthly_changes2))
print(len(month_change))

zipped_lists = zip(monthly_changes2,monthly_changes1)
changes_list = [x-y for (x,y)in zipped_lists]

print(changes_list)

print(max(changes_list))
print(min(changes_list))

average_change = sum(changes_list) / len(changes_list)
print(average_change)