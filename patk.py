#!/usr/bin/env python3

import sys
import pdb

data = open(sys.argv[1], 'r').readlines()

def patk(rankedData, num):
    negToHum =0
    negToMay = 0
    posToHum = 0
    posToMay = 0
    negToComp =0
    posToComp = 0
    # cheap and dirty code duplication
    for i in range(num):
        line = rankedData[i].split('\t')
        if line[2] == 'y' and line[3] == 'y':
            posToHum += 1
        elif line[2] == 'y' or line[3] == 'y':
            posToMay += 1
    print("p@", num, '\n',
            # "negToHum", negToHum / num, '\n',
            # "negToMay", (negToMay + negToHum) /num, '\n',
            "posToHum", posToHum / num, '\n',
            "\t", posToHum, "correct out of", num, '\n',
            "posToMay", (posToHum + posToMay) / num, '\n',
            "\t", posToHum + posToMay, "correct out of", num)#,
            # "negToComp", (negToComp + negToMay) / num, '\n')#,
            # "posToComp", posToComp / num)
            # "average", (negToComp + negToMay + posToHum) / num)

print("Highest scoring")
patk(data, 10)
patk(data, 50)
patk(data, 100)
print("Lowest scoring")
data.reverse()
patk(data, 10)
patk(data, 50)
patk(data, 100)


