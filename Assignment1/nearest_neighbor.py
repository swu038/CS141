#!/bin/py

import sys
import math 
import operator
import time

def dist(x1, y1, x2, y2):  
    return math.sqrt( (x1 - x2)*(x1 - x2) + (y1 - y2) * (y1 - y2) )  
#end dist

def brute(array): 
    min = dist(array2d[0][0], array[0][1], array2d[1][0], array2d[1][1])

    for x in range(0, len(array)):
        for y in range(x+1, len(array)): 
            if dist(array[x][0], array[x][1], array[y][0], array[y][1]) < min:
                min = dist(array[x][0], array[x][1], array[y][0], array[y][1])  
            #end if
        #end for
    #end for
    return min
#end brute

def sort(array, n):
    x = sorted(array, key=operator.itemgetter(0))  #sort by x pts
    y = sorted(array, key=operator.itemgetter(1))  #sort by y pts
    return nearest(x, y, n)
#end sort

def nearest(x, y, n): 
    if n <= 3:
        return brute(x)
    #end if

    mid = n/2
    LP = x[:mid]    #left plane 
    RP = x[mid:]    #Right plane
    
    Y_L = []        #after x divided, the sorted y of LP       
    Y_R = []        #after x divided, the sorted y of RP
    
    for p in y:
        if p in LP:
            Y_L.append(p)
        else:
            Y_R.append(p)
        #end if
    #end for
    
    dis_left = nearest(LP, Y_L, mid)
    dis_right = nearest(RP, Y_R, n-mid)
    
    min_dis = min(dis_left, dis_right)
    
    border = []      #array to check min dist b/w LP and RP
    for(i,j) in y:
        if abs( i - x[mid][0] ) < min_dis: 
            border.append((i,j))
        #end if
    #end for
     
    return min(min_dis,border_test(border, min_dis)) 
#end nearest

def border_test(border, min_dis):
    min_d = min_dis
    for i,(x,y) in enumerate(border): 
        for j in range(i+1, len(border)):
            if(border[j][1] - border[i][1]) < min_d and dist(border[i][0], border[i][1], border[j][0], border[j][1]) < min_d:
                min_d = dist(border[i][0], border[i][1], border[j][0], border[j][1])
            #end if
        #end for
    #end for
    return min_d
#end border_test

#####################################################
for i in range(1, len(sys.argv)): 
    with open(sys.argv[i], 'r') as f: 
        array2d = [[float(digit) for digit in line.split()] for line in f]
#end for

#min = dist(array2d[0][0], array2d[0][1], array2d[1][0], array2d[1][1])

size = len(array2d) 

start1 = time.time()
min = sort(array2d, size)
end1 = time.time()
print 'Divide and Conquer time: ',end1-start1

#start = time.time()
#min = brute(array2d)
#end = time.time()
#print 'Brute force time: ',end-start   

outFile = sys.argv[1].replace(".txt", "_distance.txt")
out = open(outFile, 'w') 
print >> out, min        
out.close() 
###########################################################
