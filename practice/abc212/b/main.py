#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


X = S()
# A = [LI() for _ in range(N)]
flag = 0

isSame = X[0] == X[1] and X[1] == X[2] and X[2] == X[3];

if(isSame):
    print('Weak')
else:
    for i in range(1,len(X)):
        if (int(X[i]) == int(X[i-1]) + 1) or (X[i-1] == "9" and X[i] == "0"):
            continue
        flag = 1
    if flag == 1:
        print('Strong')
    else:
        print('Weak')
