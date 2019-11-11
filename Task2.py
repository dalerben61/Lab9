import csv

fileName = input("Please enter the name of the csv file you wish to open (do not write .csv)")
csvAddToName = fileName, '.csv'
fileNameJoined = ''.join(csvAddToName)

fin = open(fileNameJoined, "r")
reader = csv.reader(fin)
next(reader,None)

for row in reader:
    print(row)

fin.close