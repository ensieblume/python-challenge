import os
import csv

# Path to collect data from the budge_data.csvr
csvpath = "budget_data.csv"


# Open the CSV
with open(csvpath, 'r') as csvfile:
    headerline = next(csvfile)
    numOfMonths = 0
    total = 0
    change = 0
    sumChange = 0
    previousValue = 0
    maxIncrease = 0
    maxDecrease = 0
    maxIncreaseDate = 0
    maxDecreaseDate = 0

    for row in csv.reader(csvfile):
        numOfMonths += 1
        total += int(row[1])

        #everytime I read a row calculate the change from the previous row
        change = int(row[1]) - previousValue
        previousValue = int(row[1]) 
       
        #The value of change is stored in second row on
        if numOfMonths > 1:
            sumChange += change

        #Finding max increase and decrease in profit and the dats associated with them
        if change > maxIncrease:
            maxIncrease = change 
            maxIncreaseDate = row[0]

        if change < maxDecrease:
            maxDecrease = change
            maxDecreaseDate = row[0] 

    #Finding the overal change. note the first row is 0, so subtract one from number of columns
    averageChange = sumChange/(numOfMonths-1)

outString = ""
outString += "Total Months: %d\n" % numOfMonths
outString += "Total: $%d\n" % total
outString += "Average Change: $%.2f\n" % averageChange
outString += "Greatest Increase in Profits: %s ($%d)\n" % (maxIncreaseDate, maxIncrease)
outString += "Greatest Decrease in Profits: %s ($%d)\n" % (maxDecreaseDate, maxDecrease)     
print(outString)
fh = open("result.txt","w")
fh.write(outString)

print("Total Months: ", numOfMonths)   
print("Total: $",total)
print("Average Change: $","%.2f"% averageChange) 
print("Greatest Increase in Profits: ",maxIncreaseDate,"($", maxIncrease,")")
print("Greatest Decrease in Profits: ",maxDecreaseDate,"($", maxDecrease,")")       

fh.write("Total Months: %d\n" % numOfMonths)   
fh.write("Total: $%d\n" % total)
fh.write("Average Change: $%.2f\n" % averageChange) 
fh.write("Greatest Increase in Profits: %s ($%d)\n" % (maxIncreaseDate, maxIncrease))
fh.write("Greatest Decrease in Profits: %s ($%d)\n" % (maxDecreaseDate, maxDecrease))     
fh.close()
