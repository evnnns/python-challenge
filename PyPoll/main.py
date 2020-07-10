import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

total_votes = 0

#Copying in CSV reader from previous exercises
with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    election_data = csv.reader(csvfile, delimiter=',')

    #Checking CSV Reader Works
    election_header = next(election_data)
    print(f'CSV Header: {election_header}')