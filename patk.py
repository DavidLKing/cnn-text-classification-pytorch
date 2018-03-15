#!/usr/bin/env python3

import sys
import pdb

data = open(sys.argv[1], 'r').readlines()

def threshold(rankedData, percent):
    total = 0
    total_may = 0
    for line in rankedData:
        line = line.split('\t')
        if line[0] == 'y' and line[1] == 'y':
            total += 1
            total_may += 1
        elif line[0] == 'y' or line[1] == 'y':
            total_may += 1
    thresh = total * percent
    thresh_may = total_may * percent
    lineNum = 0
    lineNum_may = 0
    for line in rankedData:
        line = line.split('\t')
        if thresh >  0:
            lineNum += 1
            if line[0] == 'y' and line[1] == 'y':
                thresh -= 1
                thresh_may -= 1
        else:
            continue
        if thresh_may > 0:
            lineNum_may += 1
            if line[0] == 'y' or line[1] == 'y':
                thresh_may -= 1
            else:
                continue
    print("Percent of same to get to high quality threshold:", lineNum / len(rankedData))
    print("Percent of same to get to medium quality threshold:", lineNum_may / len(rankedData))

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
        if line[0] == 'y' and line[1] == 'y':
            posToHum += 1
        elif line[0] == 'y' or line[1] == 'y':
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
threshold(data, 0.65)
print("Lowest scoring")
data.reverse()
patk(data, 10)
patk(data, 50)
patk(data, 100)
threshold(data, 0.65)


