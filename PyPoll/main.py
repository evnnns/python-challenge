import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

total_votes = 0

candidates = {}

#Copying in CSV reader from previous exercises
with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    election_data = csv.reader(csvfile, delimiter=',')

    # Checking CSV Reader Works
    election_header = next(election_data)
    # print(f'CSV Header: {election_header}')

    # Count Votes for candidates
    for row in election_data:

        total_votes = total_votes + 1

        name = row[2]
        # Adds candidates to running, adds votes to their progress
        if name not in candidates:
            candidates[name] = 1
        else:
            candidates[name] = candidates[name] + 1


print("Election Results")
print("------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------")

for candidate_name, vote_count in candidates.items():
    percentage = vote_count / total_votes * 100
    print(f'{candidate_name}: {percentage:.3f}% {vote_count}')

print("------------------------")
winner = max(candidates, key = candidates.get)    
print(f'Winner: {winner}')
print("------------------------")