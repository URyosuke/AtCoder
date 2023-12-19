#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N = I()
# A = [LI() for _ in range(N)]
i = 1
count = N
ans = 0
while count > 0:
    count = count - i
    if count <= 0:
        ans = i
        break;
    i = i + 1
    
print(ans)