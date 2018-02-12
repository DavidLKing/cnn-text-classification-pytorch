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
        if line[1] == 'negative':
            if line[5] == 'y' and line[6] == 'y':
                negToHum += 1
            elif line[5] == 'y' or line[6] == 'y':
                negToMay += 1
            else:
                assert(line[5] == 'n' or line[6] == 'n')
                negToComp += 1
        if line[1] == 'positive':
            if line[5] == 'y' and line[6] == 'y':
                posToHum += 1
            elif line[5] == 'y' or line[6] == 'y':
                posToMay += 1
            else:
                assert(line[5] == 'n' or line[6] == 'n')
                posToComp += 1
    print("p@", num, '\n',
            # "negToHum", negToHum / num, '\n',
            # "negToMay", (negToMay + negToHum) /num, '\n',
            "posToHum", posToHum / num, '\n',
            # "posToMay", posToMay / num, '\n',
            "negToComp", (negToComp + negToMay) / num, '\n')#,
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


pdb.set_trace()
