#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


# N = I()
S = [S() for _ in range(4)]
flag = 0

for i in range(4):
    for j in range(i+1,4):
        if S[i] == S[j]:
            flag = 1
if flag == 1:
    print('No')
else:
    print('Yes')
        

