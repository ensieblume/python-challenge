import os
import csv

#Path to collect Data from the election_data.csv
csvpath="election_data.csv"

#open the CSV
with open(csvpath, 'r') as csvfile:
    headerline=next(csvfile)
    totalVotes=0

    for row in csv.reader(csvfile):
        totalVotes += 1
        
    print(totalVotes)