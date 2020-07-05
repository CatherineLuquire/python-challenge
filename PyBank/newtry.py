#create python script that analyzes the records 
import os

csvpath = os.path.join('resources', 'budget_data.csv')
import csv

#with open(csvpath) as csvfile:
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)

    total = 0
    for row in csvreader:
   # total = sum(float(row[1]))
        total += int(row[1])
    
    data = list(csvreader)
    row_count=len(data)
 




print("Financial Analysis")
print("-------------------------------")   
print("Total Months: "+ str(row_count))
print("Total: " + "$" + str(total))
