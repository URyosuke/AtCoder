#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N,M = MI()
A = LI()
B = LI()

A.sort()
B.sort()

curr = 0
flag = True
i = j = 0
currAns = abs(A[i]-B[j])

while flag:
    curr = abs(A[i]-B[j])
    if curr == 0:
        currAns = 0
        break
    elif currAns > curr:
        currAns = curr
    if A[i] < B[j]:
        i += 1
    else:
        j += 1
    if i == N or j == M:
        break

print(currAns)
