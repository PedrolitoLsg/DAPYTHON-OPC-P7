import itertools
from _datetime import datetime
import csv

def brute(file):
    start = datetime.now()
    print("File used for computing is :" + str(file))
    open_file(file)
    end = datetime.now()
    duration = (end-start)
    print("Computing took:" + str(duration))
    pass


def open_file(file):
    shares = open(file)
    csvreader = csv.reader(shares)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    bruteforce(rows)
    pass



def bruteforce(rows):
    competition_list = [0]
    competition_benefit = [0]
    competition_spendings = [0]
    for elem in range(0, len(rows)+1):
       for subset in itertools.combinations(rows, elem):
           spendings = 0
           benefit = 0
           for stock in subset:
               spendings += float(stock[1])
               benefit += (float(stock[1]) * (float(stock[2])/100))
           if benefit > competition_benefit[0]:
               if spendings <= 500:
                   del competition_list[0]
                   competition_list.append(subset)
                   del competition_benefit[0]
                   competition_benefit.append(benefit)
                   del competition_spendings[0]
                   competition_spendings.append(spendings)
    print("Best Combination gives a benefit of: " + str(competition_benefit) + " euros \n"
          + "The list of shares is" + str(competition_list) + "\n"
          + "total cost = " + str(competition_spendings) + " euros")
    pass