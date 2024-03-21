import os
import csv

Stockham = []
DeGette = []
Doane = []
Typo = []

# Note: must run from PyPoll folder
PyPoll = os.path.join("Resources","election_data.csv")

with open(PyPoll, encoding='UTF-8') as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:          
        if row[2] == "Charles Casper Stockham":
            S = Stockham.append(row[2])
        elif row[2] == "Diana DeGette":
            De = DeGette.append(row[2])
        elif row[2] == "Raymon Anthony Doane":
            Do = Doane.append(row[2])
        else:
            T = Typo.append(row[2])

    StockhamTotal = len(Stockham) 
    DeGetteTotal = len(DeGette)
    DoaneTotal = len(Doane) 
    NumTypo = len(Typo)
    
    print (f'The number of typos in the list was {NumTypo}')  
    # Output to terminal verified that there were no typos in the Candidate column

    TotalVotes = StockhamTotal + DeGetteTotal + DoaneTotal 
    StockhamPerc = round((StockhamTotal / TotalVotes * 100),3)
    DeGettePerc = round((DeGetteTotal / TotalVotes * 100), 3)
    DoanePerc = round((DoaneTotal / TotalVotes * 100), 3)
    Winner = max(StockhamTotal, DeGetteTotal, DoaneTotal)

    candidates = [['Charles Casper Stockham', StockhamTotal], ['Diana DeGette', DeGetteTotal], ["Raymon Anthony Doane", DoaneTotal]]
    for i, sublist in enumerate(candidates):
        if Winner in sublist:
            WinnerName = candidates[i][0]

    Lines = [
        (f"Election Results"),
        (f"---------------------------------------"),
        (f'Total Votes: {TotalVotes}'),
        (f"---------------------------------------"),
        (f'{candidates[0][0]}: {StockhamPerc}% ({StockhamTotal})'),
        (f'{candidates[1][0]}: {DeGettePerc}% ({DeGetteTotal})'),
        (f'{candidates[2][0]}: {DoanePerc}% ({DoaneTotal})'),
        (f'---------------------------------------'),
        (f'Winner: {WinnerName}')
    ]

    for line in Lines:
        print (line)

    output_path = os.path.join("Analysis","Election_Results.txt")
    with open(output_path, 'w') as file:
        for line in Lines:
            file.write(line)
            file.write("\r")