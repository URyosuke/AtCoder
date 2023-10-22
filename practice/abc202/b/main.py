#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = S()
# A = [LI() for _ in range(N)]
ans = []
for x in N:
    if x == '0':
        ans.append('0')
    elif x == '1':
        ans.append('1')
    elif x == '6':
        ans.append('9')
    elif x == '8':
        ans.append('8')
    elif x == '9':
        ans.append('6')
# .reverse()で返る値はNone       
ans.reverse()
print(''.join(ans))