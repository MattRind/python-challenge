import os
import csv

# Lists to store data
Dates = []
ProfitLoss = []
Profit_Loss_change = []

Total_PL = 0
previous = 0
Sum_Delta_PL = 0
Delta_PL = 0

# Note: must run from PyBank folder
PyBank = os.path.join("Resources","budget_data.csv")

with open(PyBank, encoding='UTF-8') as csvfile:
    
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:  
        d = Dates.append(row[0])
        pl = ProfitLoss.append(row[1])  
    
        Total_PL = int(row[1]) + Total_PL      # cannot convert to int() nor use sum() w/ row[1] CSV data
        Delta_PL = Profit_Loss_change.append(int(row[1]) - previous)
        Sum_Delta_PL = (int(row[1])-previous) + Sum_Delta_PL
        previous = int(row[1])
        
    Profit_Loss_change.pop(0)    # remove first datapoint in set, which is actually just the first PL value
    Total_Months = len(Dates)
    Average_Change = round(sum(Profit_Loss_change)/(len(Profit_Loss_change)),2)
    Great_PL_Increase = max(Profit_Loss_change)
    Great_PL_Decrease= min(Profit_Loss_change)
    maxindex = Profit_Loss_change.index(Great_PL_Increase) + 1   #indexes of CSV data & PL Change are offset
    minindex = Profit_Loss_change.index(Great_PL_Decrease) + 1
    Great_PL_Increase_Date = Dates[maxindex]
    Great_PL_Decrease_Date = Dates[minindex]

    Lines = [
        (f'Total Months: {Total_Months}'),
        (f'Total: ${Total_PL}'),
        (f'Average Change: ${Average_Change}'),
        (f'Greatest Increase in Profits: {Great_PL_Increase_Date} (${Great_PL_Increase})'),
        (f'Greatest Decrease in Profits: {Great_PL_Decrease_Date} (${Great_PL_Decrease})')
    ]
    for line in Lines:
        print (line)

    output_path = os.path.join("Analysis","Financial_Analysis.txt")
    with open(output_path, 'w') as file:
        file.write("Financial Analysis")
        file.write("\r")
        file.write("--------------------------")
        file.write("\r")
        for line in Lines:
            file.write(line)
            file.write("\r")
