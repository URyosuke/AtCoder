#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


D = I()
if math.sqrt(D) == math.floor(math.sqrt(D)):
    print(0)
    sys.exit()

x = math.ceil(math.sqrt(D))
x_2 = x * x
currentAns = 10**18

for i in range(x+1):
    resid = D-i**2
    if resid < 0:
        y=0
    else:
        y_ceil = math.ceil(math.sqrt(resid))
        y_floor = math.floor(math.sqrt(resid))
        if abs(resid-y_ceil**2) < abs(resid-y_floor**2):
            y = y_ceil
        else:
            y = y_floor
        currentAns = min(currentAns, abs(D-i**2-y**2))

print(currentAns)