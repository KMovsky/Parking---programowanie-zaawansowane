import numpy as np #listy i arraye
import os #obsluga systemu i plikow
import sklearn #sci-kit learn
import matplotlib.pyplot as plt
import random
import re #regular expressions

#dataset.csv:
#SystemCodeNumber,Capacity,Occupancy,LastUpdated

filepath = 'd:\\dev\\modelowanie\\dataset.csv'

datafile = open(filepath, 'r')
lines=datafile.readlines()



#with open (filepath, 'r') as datasheet:
#    content=datasheet.read()
#    lines=datasheet.readlines()
count = 0

Parking_Spots = []

for line in lines:
    #print(line.split(',')[0])
    if line.split(',')[0] == 'BHMBCCMKT01':
        print(line.split(',')[2])


    if line.split(',')[0] not in Parking_Spots:
        print(str(count))
        Parking_Spots.append(line.split(',')[0])
        print(str(line.split(',')[0]))
        count = 1
    else:
        count += 1
    #if (line.split(',')[0] != line.split(',')[0]):
     #   print(str(count))
    



    
print(Parking_Spots)

#regex = re.compile(r'\s\w+,')
#mo = regex.search(content)
#print(mo)



#print(content)


datafile.close()