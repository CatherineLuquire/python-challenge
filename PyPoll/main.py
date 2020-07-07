#import csv
import os
from collections import Counter
csvpath = os.path.join('resources', 'election_data.csv')
import csv

print("Election Results")
print("-----------------------")

#set variables and lists
# total_votes = 0
can_count = []
# candidates = {}
# can_0_votes = 0
# can_1_votes = 0
# can_2_votes = 0
# can_3_votes = 0
# percentages = []

# with open(csvpath, 'r') as text:
#     csvreader = csv.reader(text, delimiter=',')
#     lines=text.read()

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    #read(csvfile, delimiter=',')
    csv_header = next(csvreader) 
    #print(csv_header)
#find total number of votes cast
    for row in csvreader:
        can_count.append(row[2])
    #     row_voterid = row[0]
    # #     row_county = row[1]
    #     row_candidate = row[2]
    # #     #row_candidate = text.read()
    # #     #print(row_candidate)
    #     if row_candidate not in candidates:
    #         candidates.append(row_candidate)
    #   total_votes = total_votes + 1
    candidates = Counter(can_count)
    total_votes = (sum(candidates.values()))
    print("Total Votes: " + str(total_votes))
    print("-----------------------")
    winner = (max(candidates, key=candidates.get))

    # for value in candidates.items():
    #     print((value/total_votes)*100)

    
    for key, value in candidates.items():
       # for i in range(len(candidates)):
        percentage = round(((value / total_votes) * 100),4 )
        print(key + ": ", str((percentage)) + "%", value)
       # print(key + ": ", str(((value / total_votes) * 100)) + "%", value)
    print("-----------------------")
    print("Winner: " + winner)
    print("-----------------------")
    #print((([value for value in candidates.values()][1]) / total_votes) * 100)
    #print(max(candidates.values()))
    #print("Total Votes: "+ str(total_votes))
    #print(candidates)
    # print(row_candidate)
    # a = range((len(can_count)))
    # b = range((len(candidates)))
    # for i, x in a, b: 
    # for i in range((len(can_count))):
    #     if can_count[i] == candidates[0]: 
    #         can_0_votes = can_0_votes + 1
    #     elif can_count[i] == candidates[1]:    
    #         can_1_votes = can_1_votes + 1
    #     elif can_count[i] == candidates[2]:    
    #         can_2_votes = can_2_votes + 1
    #     else:
    #         can_3_votes = can_3_votes + 1

    # percent_0 = round(can_0_votes / total_votes *100,4)
    # percent_1 = round(can_1_votes / total_votes *100,4)
    # percent_2 = round(can_2_votes / total_votes *100,4)
    # percent_3 = round(can_3_votes / total_votes *100,4)

    # percentages = [percent_0, percent_1, percent_2, percent_3]
    # max_percent = percentages.index(max(percentages))
    # winner = candidates[max_percent]
    
    # print(candidates[0] + ": " + str(percent_0) + "% (" + str(can_0_votes) + ")")
    # print(candidates[1] + ": " + str(percent_1) + "% (" + str(can_1_votes) + ")")
    # print(candidates[2] + ": " + str(percent_2) + "% (" + str(can_2_votes) + ")")
    # print(candidates[3] + ": " + str(percent_3) + "% (" + str(can_3_votes) + ")")
    # print("------------------------------")
    # print("Winner: " + str(winner))

    
#compile a list of candidates who received votes
#calculate percentages of votes each candidate won
#total number of votes each candidate won
#winner of election based on popular vote
#  Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------