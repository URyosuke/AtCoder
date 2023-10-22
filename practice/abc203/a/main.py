#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
# 入力の受け取り
a,b,c = MI()
if a == b:
    print(str(c))
elif a == c:
    print(str(b))
elif b == c:
    print(str(a))
else:
    print(0)