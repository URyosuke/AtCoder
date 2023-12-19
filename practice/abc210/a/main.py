#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N,A,X,Y = MI()
# A = [LI() for _ in range(N)]

ans = 0

for i in range(1,N+1):
    if i <= A:
        ans += X
    else:
        ans += Y
print(ans)
