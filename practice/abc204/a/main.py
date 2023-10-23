#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


# N = I()
# A = [LI() for _ in range(N)]
x,y = LI()

if x == y:
    z = x
elif x+y == 1:
    z = 2
elif x + y == 2:
    z = 1
else:
    z = 0
print (z)