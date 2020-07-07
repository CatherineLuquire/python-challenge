#import csv
import os
#import counter function
from collections import Counter
csvpath = os.path.join('resources', 'election_data.csv')
import csv

print("Election Results")
print("-----------------------")

# set list for total candidate vote counts
can_count = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    # pass csv header
    csv_header = next(csvreader) 

    # use a for loop to add all votes to can_count
    for row in csvreader:
        can_count.append(row[2])
    # use counter function to count all votes and create dictionary
    candidates = Counter(can_count)
    # calculate total votes cast
    total_votes = (sum(candidates.values()))
    
    # use max function to find the key of the candidate with the most votes
    winner = (max(candidates, key=candidates.get))

    # print results to terminal and text file
    with open("Analysis/output.txt", "w") as text_file:
        print("Total Votes: " + str(total_votes))
        print("Total Votes: " + str(total_votes), file=text_file)        
        print("-----------------------")
        print("-----------------------", file=text_file)
        # use a for loop to calculate the percentage of the vote each candidate received and print
        for key, value in candidates.items():
            percentage = round(((value / total_votes) * 100),4 )
            print(key + ": ", str((percentage)) + "%", value)
            print(key + ": ", str((percentage)) + "%", value, file=text_file)

        print("-----------------------")
        print("-----------------------", file=text_file)
        print("Winner: " + winner)
        print("Winner: " + winner, file=text_file)
        print("-----------------------")
        print("-----------------------", file=text_file)
