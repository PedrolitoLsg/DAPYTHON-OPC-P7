from bruteforce import brute
from optimized import opti

file1 = 'csv1.csv'
file2 = 'dataset1_Python+P7.csv'
file3 = 'dataset2_Python+P7.csv'

text_1 = "Press 1 for bruteforce, 2 for the greedy algo"
text_2 = "1 for the 20 action dataset, 2 for the first giant dataset, 3 for the other big dataset"

def home():
    print(text_1)
    answer = int(input())
    if answer == 1:
        print(text_2)
        file = int(input())
        if file == 1:
            brute(file1)
        elif file == 2:
            brute(file2)
        elif file == 3:
            brute(file3)

    elif answer == 2:
        print(text_2)
        file = int(input())
        if file == 1:
            opti(file1)
        elif file == 2:
            opti(file2)
        elif file == 3:
            opti(file3)
    pass

home()