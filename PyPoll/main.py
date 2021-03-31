import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    casted_votes = 0
    for row in csvreader:
        casted_votes += 1

#A complete list of candidates who received votes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    candidates = []

    for vote in csvreader:
        if  str(vote[2]) not in candidates:
            candidates.append(vote[2])
            
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    vote_count  = [0,0,0,0]

    for vote in csvreader:
        if  str(vote[2]) == str(candidates[0]):
            vote_count[0] += 1
        elif  str(vote[2]) == str(candidates[1]):
            vote_count[1] += 1    
        if  str(vote[2]) == str(candidates[2]):
            vote_count[2] += 1 
        if  str(vote[2]) == str(candidates[3]):
            vote_count[3] += 1
    

#The winner of the election based on popular vote.
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
percentages = []
for x in range(len(candidates)):
    percentages.append((vote_count[x])/casted_votes)

print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {casted_votes}")
print("-------------------------")
print(candidates)
print(vote_count)


for x in range(len(candidates)):
    print(f"{candidates[x]} : ({vote_count[x]})")

#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------


