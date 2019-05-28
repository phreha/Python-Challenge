import csv
import os

# create file path and save as file
file = os.path.join('..', 'Resources', 'budget_data.csv')

#lists for month and profit data
months = []
profit = []

#read csv and parse data into lists
#profit list will be list of integers
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        profit.append(int(row[1]))

#find total months
total_months = len(months)

#create greatest increase, decrease variables and set them equal to the first profit entry
#set total profit = 0 
greatest_inc = profit[0]
greatest_dec = profit[0]
total_profit = 0

#loop through profit indices and compare # to find greatest inc and dec
#also add each profit to total profit
for r in range(len(profit)):
    if profit[r] >= greatest_inc:
        greatest_inc = profit[r]
        great_inc_month = months[r]
    elif profit[r] <= greatest_dec:
        greatest_dec = profit[r]
        great_dec_month = months[r]
    total_profit += profit[r]

#calculate average_change
average_change = round(total_profit/total_months, 2)

#sets path for output file
output_path = os.path.join('..', 'Output', 'analysis.csv')

# opens the output destination in write mode and prints the summary
with open(output_path, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total: $' + str(total_profit) + '\n')
    writefile.writelines('Average Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#opens the output file in r mode and prints to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())