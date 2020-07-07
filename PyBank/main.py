#create python script that analyzes the records 
#import os and csv
import os

csvpath = os.path.join('resources', 'budget_data.csv')
import csv

# create lists to store revenue, dates, and monthly revenue change 
revenue = []
date = []
rev_change_lst = []

# with open(csvpath) as csvfile:
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # pass csv header
    csv_header = next(csvreader) 

    # create loop to populate the date and revenue lists with dates and revenues from csv file
    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])

    # calculate the montly revenue change and populate rev_change_lst
    for i in range(int(len(revenue)-1)):
        revenue_change = (revenue[i+1]) - (revenue[i])
        rev_change_lst.append(revenue_change)
        # use rev_change_list to calculate total months, to p&l, average monthly change, and greatest increase & decrease in profits
        sum_rev_change = sum(rev_change_lst)
        len_rev_change = len(rev_change_lst)
        avg_rev_change = sum_rev_change / len_rev_change
        max_rev_change = max(rev_change_lst)
        min_rev_change = min(rev_change_lst)
        # use index of max  & min rev_change to print associated month
        max_index = rev_change_lst.index(max(rev_change_lst))
        min_index = rev_change_lst.index(min(rev_change_lst))

# print to a new text file
with open("Analysis/output.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print("Total Months: " +str(len(date)), file=text_file)
    print("Total: $" + str(round(sum(revenue))), file=text_file)
    print("Average Change: $" + str(round(avg_rev_change)), file=text_file)
    print("Greatest Increase in Profits: " + str(date[max_index +1]) + " $" + str(max_rev_change), file=text_file)
    print("Greatest Decrease in Profits: " + str(date[min_index +1]) + " $" + str(min_rev_change), file=text_file)

# print results
print("Financial Analysis")
print("----------------------------")
print("Total Months: " +str(len(date)))
print("Total: $" + str(round(sum(revenue))))
print("Average Change: $" + str(round(avg_rev_change)))
print("Greatest Increase in Profits: " + str(date[max_index +1]) + " $" + str(max_rev_change))
print("Greatest Decrease in Profits: " + str(date[min_index +1]) + " $" + str(min_rev_change))
