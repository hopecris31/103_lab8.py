#Hope Crisafi
#Lab 8
#5/19/21

#NJW 7/10

#NJW You include shark attacks that are NOT in the USA (-1)
#NJW You don't tell me the average per year (-1)
#NJW Why two for loops for the stock price? Can't you do it all in one?
#NJW You don't tell me the DATE of the max google price (-1)

import csv

filename = 'GOOG.csv'
myFile = open(filename, 'r')
stocks = csv.reader(myFile)

#Headers are stock information categories; Their order is:
#Date, Open, High, Low, Close, Adj Close, and Volume

next(stocks) #have to put before iteration

#for date in stocks:
#    print('line is: ',date)

myFile.close()

myFile = open(filename, 'r')
stocks = csv.reader(myFile)

#date(0), close(4), volume(6)
total = 0
counter = 0
highestPrice = 0

next(stocks)
for close in stocks:
    total = float(close[4]) + total
    counter += 1
    highestPrice = max(float(close[4]),highestPrice)
    #compares two values, highest price (which is 0) and the values in the fourth column
    averagePrice = total / counter
    daysOnMarket = counter

myFile.close()

#have to close and reopen file, python can only iterate the file once per open

myFile = open(filename, 'r')
stocks = csv.reader(myFile)

totalDays = 0
counter = 0
trades = 0

next(stocks)
for days in stocks:
    trades = float(days[6]) + trades
    counter += 1
    averageTrades = trades / counter

print('max is: ',highestPrice)
print('average price is: ', averagePrice)
print('average trades per day: ',averageTrades)
print('total days on market: ',counter)

myFile.close()


#averagePrice = total / counter
#averageTrades = plug in index 6 for vol column, use another for loop 
#daysOnMarket = use counter to count columns



#Part 2


filename = 'sharks.csv'
sharkFile = open(filename, 'r', encoding='ISO-8859-1"')
sharks = csv.reader(sharkFile)

unprovokedAttacks = 0


next(sharks) #skip the heading rows for reading data
for attacks in sharks:
    #make the values of the column integers so it can compare, only looking at dates after 1990
    if int(attacks[1]) > 1990:
        #if the attack column says unprovoked, add 1 to the counter
        if (attacks[2]) == 'Unprovoked':
            unprovokedAttacks += 1

print('unprovoked attacks: ', unprovokedAttacks)

sharkFile.close()

#how many attacks were unprovoked
