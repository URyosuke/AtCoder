#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N,L,R = MI()
A = LI()

for i in range(N):
    if i == N-1:
        if A[i] <= (L):
            print(L)
        elif A[i] >= (R):
            print(R)
        else:
            print(A[i])
    else:
        if A[i] <= (L):
            print(L,end=' ')
        elif A[i] >= (R):
            print(R,end=' ')
        else:
            print(A[i],end=' ')
    
