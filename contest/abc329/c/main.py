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
S = S()

from collections import defaultdict
d = defaultdict(int)

if len(S) == 1:
    print(1)
    sys.exit()

alpha = list(string.ascii_lowercase)

for key in alpha:
    d[key] = 0

for str in alpha:
    count = 0
    for i in range(N):
        if str == S[i]:
            count += 1
        else:
            count = 0
        if d[str] < count:
            d[str] = count
        


ans = 0
for str in alpha:
    ans += d[str]

print(ans)
        
