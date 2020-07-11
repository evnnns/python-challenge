import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
net_pnl = 0


with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budget = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    budget_header = next(budget)
    # print(f"Budget Header: {budget_header}")

    for month in budget:
        
        # Counts how many months long the period is
        total_months = total_months + 1

        # Sums all PnL data
        net_pnl = net_pnl + float(month[1])

        



print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_pnl}')

