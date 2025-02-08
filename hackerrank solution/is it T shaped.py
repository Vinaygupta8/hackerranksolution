#!/bin/python3

import math

import os
import random
import re
import sys

# Complete the solve function below.
def solve(grid):
    x=[]
    y=[]
    for i in grid:
        x.append(i[0])
        y.append(i[1])
    xmin=min(x)
    ymin=min(y)
    x=[i-xmin for i in x]
    y=[i-ymin for i in y]
    for i in x:
        if i>2:
            return("No")
    for i in y:
        if i>2:
            return("No")
    b=[]
    for i in range(5):
        b.append([x[i],y[i]])
    
    
    if([0,2]not in b and[0,0] not in b and [1,2]not in b and[1,0]not in b):
        return('Yes')
    if([0,2]not in b and[0,1] not in b and [2,2]not in b and[2,1]not in b):
        return('Yes')
    if([2,2]not in b and[2,0] not in b and [1,2]not in b and[1,0]not in b):
        return('Yes')
    if([0,1]not in b and[0,0] not in b and [2,1]not in b and[2,0]not in b):
        return('Yes')
    else:
        return("No")
        
        
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        points = []

        for _ in range(5):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)

        fptr.write(result + '\n')

    fptr.close()
