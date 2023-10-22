#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N, K = MI();
friends = [LI() for _ in range(N)]

friends.sort()
currVillage = K

for i in range(N):
    friendVillage=friends[i][0]
    friendMoney = friends[i][1]
    
    if friendVillage <= currVillage:
        currVillage += friendMoney
    else:
        break
print(currVillage);