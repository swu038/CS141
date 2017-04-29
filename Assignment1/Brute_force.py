#!/bin/py

import sys
import math
import time

def dist(x1, y1, x2, y2):  
    return math.sqrt( (x1 - x2)*(x1 - x2) + (y1 - y2) * (y1 - y2) )  
#end def

for i in range(1, len(sys.argv)): 
    with open(sys.argv[i], 'r') as f: 
        array2d = [[float(digit) for digit in line.split()] for line in f]
#end for

start = time.time()
min = dist(array2d[0][0], array2d[0][1], array2d[1][0], array2d[1][1])

for x in range(0, len(array2d)):
    for y in range(x+1, len(array2d)): 
        if dist(array2d[x][0], array2d[x][1], array2d[y][0], array2d[y][1]) < min:
            min = dist(array2d[x][0], array2d[x][1], array2d[y][0], array2d[y][1])  
        #end if
    #end for
#end for

outFile = sys.argv[1].replace(".txt", "_distance.txt")
out = open(outFile, 'w') 
print >> out, min           #prints min to outFile
out.close() 
end = time.time()
print end-start

#print array2d[0][0]
#print array2d[0][1]
#print array2d[1][0]
#print array2d[1][1]
#print array2d[2][0]
#print array2d[2][1]   
