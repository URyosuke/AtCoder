#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N,K = LI()
aa = LI()

a = [[0,i]for i in range(N)]
for i in range(N):
    a[i][0] =  aa[i]
    # a[i].append(i)

a = sorted(a, reverse=False, key=lambda x: x[0])

eq = (K // N)
amari = K % N

for i in range(N):
    a[i][0] = eq

for i in range(amari):
    a [i][0] += 1

a = sorted(a,reverse=False, key=lambda x: x[1])

for i in range(N):
    print(a[i][0])