from os import *
from sys import *
from collections import *
from math import *




#Write your printDivisors function here.
import math


def printDivisors(n):
    arr=[]
    sz =int(math.sqrt(n))
    #print(sz)
    for i in range(1,sz+1):
        if n%i == 0:
            arr.append(i)
            if int(n/i) != i:
                arr.append(int(n/i))

    arr.sort()

    for i in arr:
        print(i,end=' ')






n = int(input())
printDivisors(n)