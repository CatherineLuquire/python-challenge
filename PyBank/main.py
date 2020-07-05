#create python script that analyzes the records 
import os

csvpath = os.path.join('resources', 'budget_data.csv')
import csv

print("Financial Analysis")
print("----------------------------")

# total_months = 0
# total_pl = 0
revenue = []
date = []
rev_change_lst = []
# greatest_inc = 0
# greatest_dec = 0

#with open(csvpath) as csvfile:
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    csv_header = next(csvreader) 
    # print(csv_header)

    # calculate the net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])
        # row_dt = row[0]
        # row_n = int(row[1])
        # total_months = total_months + 1
        # total_pl = total_pl + row_n
     #   print(str(revenue))
    for i in range(int(len(revenue)-1)):
        revenue_change = (revenue[i+1]) - (revenue[i])
        rev_change_lst.append(revenue_change)
        #print(revenue_change)
        sum_rev_change = sum(rev_change_lst)
        len_rev_change = len(rev_change_lst)
        avg_rev_change = sum_rev_change / len_rev_change
        max_rev_change = max(rev_change_lst)
        max_index = rev_change_lst.index(max(rev_change_lst))
        #print(str(max_index))
        #max_row = max_index
        #print(date[max_index + 1])
        min_rev_change = min(rev_change_lst)
        min_index = rev_change_lst.index(min(rev_change_lst))

        #print(row_dt)
    #     total_months = row + 
    #     total = sum(int(row[1]))
    # print(str(total))


#the average of the changes in "Profits/Losses" over the period

#the greatest increase in profits (Date and amount) over the period

#the greatest decrease in losses (date and amount) over the entire period

# look like this:
# print("Total Months: " + str(total_months))
# print("Total: $" + str(total_pl))
print("Total Months: " +str(len(date)))
print("Total: $" + str(round(sum(revenue))))
print("Average Change: $" + str(round(avg_rev_change)))
print("Greatest Increase in Profits: " + str(date[max_index +1]) + " $" + str(max_rev_change))
print("Greatest Decrease in Profits: " + str(date[min_index +1]) + " $" + str(min_rev_change))

#Total Months: 86
#Total: $38382578
#Average Change: $-2315.12
#Greatest Increase in Profits: Feb 2012 ($1926159)
#Greatest Decrease in Profits: Sept-2013 (-$2196167)
#output to a new file   
