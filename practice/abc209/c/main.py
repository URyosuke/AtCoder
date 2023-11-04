#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N = I()
C = LI()

ans= 1
mod = 10 ** 9 + 7
C.sort()

for i in range(N):
    if C[i] -i == 0:
        print(0)
        exit()
    ans *= C[i] - i
    ans%=mod
print(ans)
