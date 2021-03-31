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

n = len(monthly_changes2)
monthly_changes1.pop(n)

zipped_lists = zip(monthly_changes2,monthly_changes1)
changes_list = [x-y for (x,y)in zipped_lists]

average_change = sum(changes_list) / len(changes_list)

maxposition = (max(changes_list))
minposition = (min(changes_list))

position_month1 = changes_list.index(maxposition)
position_month2 = changes_list.index(minposition)

maxmonth = (month_change[position_month1])
minmonth = (month_change[position_month2])

print("--------------------------------------------------------")
print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: $ {total}")
print(f"Average  Change: $ {average_change:.2f}")
print(f"Greatest Increase in Profits: {maxmonth} with ${max(changes_list)}")
print(f"Greatest Decrease in Profits: {minmonth} with ${min(changes_list)}")
print("--------------------------------------------------------")
print(" ")
print(" ")


output_path = os.path.join( "analysis", "Financial_analysis.txt")

with open(output_path, 'w') as result:

    result.write("--------------------------------------------------------")
    result.write("\nFinancial Analysis")
    result.write("\n--------------------------------------------------------")
    result.write(f"\nTotal Months: {month_count}")
    result.write(f"\nTotal: $ {total}")
    result.write(f"\nAverage  Change: $ {average_change:.2f}")
    result.write(f"\nGreatest Increase in Profits: {maxmonth} with ${max(changes_list)}")
    result.write(f"\nGreatest Decrease in Profits: {minmonth} with ${min(changes_list)}")
    result.write("\n--------------------------------------------------------")

print(f"Results are now available: {output_path}")