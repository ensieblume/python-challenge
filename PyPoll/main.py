import os
import csv

#Path to collect Data from the election_data.csv
csvpath="election_data.csv"

#open the CSV
with open(csvpath, 'r') as csvfile:
    
    headerline=next(csvfile)
    #creating empty dictionary and initilaizing values to zero
    numOfVotes={}
    totalVotes=0
    winnerValue=0
    winnerName = 0
    
    outString = ""
    outString += "Election Results\n"
    outString += "----------------------\n"
    for row in csv.reader(csvfile):
        totalVotes += 1

        #name of the candidates are in third column which is row[2]
        candidate = row[2]
        if candidate in numOfVotes:
            numOfVotes[candidate] += 1
        else:
            numOfVotes[candidate] = 1
    outString += "Total Votes: %d\n" % totalVotes
    outString += "----------------------\n"

    #key and corresponding value can be retrieved
    # at the same time using the items() method.
    for k, v in numOfVotes.items():

        #formatting decimal to percent and outputing the values
        percentCandidate = '{0:.3f}%'.format((v/totalVotes)*100)

        outString += "%s: %.3f%s %s%d%s\n" % (k, (v/totalVotes)*100, "%", "(", v, ")")
        
     
        if v > winnerValue:
            winnerValue = v
            winnerName = k
    
    outString += "----------------------\n"
    outString += "Winner: %s\n" % winnerName
    outString += "----------------------\n"
    print(outString)
    fh = open("result.txt","w")
    fh.write(outString)
    fh.close()
    


        