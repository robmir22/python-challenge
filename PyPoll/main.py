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
    
    vote_count  = []
    for x in range(len(candidates)):
        vote_count.append(0)


    for vote in csvreader:
        if  str(vote[2]) == str(candidates[0]):
            vote_count[0] += 1
        elif  str(vote[2]) == str(candidates[1]):
            vote_count[1] += 1    
        if  str(vote[2]) == str(candidates[2]):
            vote_count[2] += 1 
        if  str(vote[2]) == str(candidates[3]):
            vote_count[3] += 1
    
percentages = []
for x in range(len(candidates)):
    percentages.append((vote_count[x])/casted_votes*100)

winner = max(vote_count)
winner_position = vote_count.index(winner)
winnerwinner = candidates[winner_position]


print("--------------------------------------")
print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {casted_votes}")
print("--------------------------------------")
for x in range(len(candidates)):
    print(f"{candidates[x]}: {percentages[x]:.2f}% ({vote_count[x]} votes)")
print("--------------------------------------")
print(f"The winner is: {winnerwinner}")
print("--------------------------------------")

output_path = os.path.join( "analysis", "Election_Results.txt")

with open(output_path, 'w') as result:

    result.write("--------------------------------------\n")
    result.write("Election Results\n")
    result.write("--------------------------------------\n")
    result.write(f"Total Votes: {casted_votes}\n")
    result.write("--------------------------------------\n")
    for x in range(len(candidates)):
        result.write(f"{candidates[x]}: {percentages[x]:.2f}% ({vote_count[x]} votes)\n")
    result.write("--------------------------------------\n")
    result.write(f"The winner is: {winnerwinner}\n")
    result.write("--------------------------------------\n")
print("")
print(f"Results are now available: {output_path}")