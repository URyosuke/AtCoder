#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N = I()
kukan = [LI() for _ in range(N)]

for i in range(N):
    if kukan[i][0] == 2:
        kukan[i][2] = kukan[i][2] - 0.1
    elif kukan[i][0] == 3:
        kukan[i][1] = kukan[i][1] + 0.1
    elif kukan[i][0] == 4:
        kukan[i][1] = kukan[i][1] + 0.1
        kukan[i][2] = kukan[i][2] - 0.1
ans = 0
for i in range(N):
    for j in range(i+1,N):
        if kukan[j][1] <= kukan[i][2] <= kukan[j][2]:
            ans += 1
        elif kukan[j][1] <= kukan[i][1] <= kukan[j][2]:
            ans += 1
        elif kukan[i][1] <= kukan[j][1] <= kukan[i][2]:
            ans += 1
        elif kukan[i][1] <= kukan[j][2] <= kukan[i][2]:
            ans += 1
print(ans)
        

