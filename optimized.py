from _datetime import datetime
import csv

piggy_bank = 500


def opti(file):
    start = datetime.now()
    print("File used for computing is :" + str(file))
    open_file(file)
    end = datetime.now()
    duration = (end - start)
    print("Computing took:" + str(duration))
    pass


def open_file(file):
    shares = open(file)
    csvreader = csv.reader(shares)
    header = next(csvreader)
    '''Appending new rows and modifying them to be integers'''
    rows = []
    for row in csvreader:
        if float(row[1]) > 0:
            new_row = []
            new_row.append(str(row[0]))
            new_row.append(float(row[1]))
            new_row.append(float(row[2]))
            rows.append(new_row)
    optimized(rows)
    pass


def optimized(rows):
    '''first sort by benefit and then by price'''
    sorted_list = sorted(sorted(rows, key=lambda x: x[1], reverse=True), key=lambda x: x[2], reverse=True)
    choice_list = []
    benefit = 0
    spendings = 0
    for elem in sorted_list:
            if (spendings + elem[1] <= piggy_bank):
                choice_list.append(elem)
                spendings += elem[1]
                benefit += (elem[1]) * (elem[2]/100)
                if spendings == piggy_bank:
                    break
    print("Best Combination gives a benefit of: " + str(benefit) + " euros \n"
          + "The list of shares is" + str(choice_list) + "\n"
          + "total cost = " + str(spendings) + " euros")
    pass
