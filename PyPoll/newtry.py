#import csv
import os

csvpath = os.path.join('resources', 'election_data.csv')
import csv

print("Election Results")
print("-----------------------")

candidate_data = {"name":, "vote_count":}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    #read(csvfile, delimiter=',')
    csv_header = next(csvreader) 
    #print(csv_header)
#find total number of votes cast
    for row in csvreader:
        candidate_count = row[2]
        if candidate_count not in candidate_data:
            candidate_data[row2] =  
        can_count.append(row[2])
    #     row_voterid = row[0]
    #     row_county = row[1]
    #     #row_candidate = text.read()
    #     #print(row_candidate)
        total_votes = total_votes + 1

    print("Total Votes: "+ str(total_votes))