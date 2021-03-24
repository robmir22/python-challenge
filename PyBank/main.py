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

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    month_count = 0
    total = 0
    for row in csvreader:
        month_count += 1
        total += int(row[1])
    print(month_count)
    print(total)
