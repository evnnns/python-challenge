import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')
analysis = os.path.join('analysis', 'budget_analysis.txt')

total_months = 0
net_pnl = 0
pnl_data = []
pnl_change = 0


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

        if pnl_change == 0:
            pnl_change = float(month[1])
        else:
            pnl_change = float(month[1]) - pnl_change
            pnl_data.append(pnl_change)
            pnl_change = float(month[1])

average_change = sum(pnl_data) / len(pnl_data)
with open(analysis, 'w') as txt:
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_pnl:.2f}')
    print(f'Average Change: ${average_change:.2f}')
    print(f'Greatest Increase in Profits: ${max(pnl_data):.2f}')
    print(f'Greatest Decrease in Profits: ${min(pnl_data):.2f}')

    print("Financial Analysis", file=txt)
    print("----------------------------", file=txt)
    print(f'Total Months: {total_months}', file=txt)
    print(f'Total: ${net_pnl:.2f}', file=txt)
    print(f'Average Change: ${average_change:.2f}', file=txt)
    print(f'Greatest Increase in Profits: ${max(pnl_data):.2f}', file=txt)
    print(f'Greatest Decrease in Profits: ${min(pnl_data):.2f}', file=txt)