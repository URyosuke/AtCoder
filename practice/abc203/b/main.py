#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
# N = I()
# A = [LI() for _ in range(N)]

N,K = MI();
sum = 0
for i in range(N):
    for j in range(K):
        sum += ((i + 1) * 100) + (j + 1)
print(sum)