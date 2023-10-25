#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


A,B,C = LI()
# A = [LI() for _ in range(N)]
A_minus = False
B_minus = False

if A < 0:
    A_minus = True
if B < 0:
    B_minus = True

A = abs(A)
B = abs(B)

if C % 2 == 0:
    
    if (A) > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('=')
else:
    if A_minus & B_minus:
        if A > B:
            print('<')
        elif A < B:
            print('>')
        else:
            print('=')
        
    elif A_minus:
        print('<')
    elif B_minus:
        print('>')
    else:
        if (A) > B:
            print('>')
        elif A < B:
            print('<')
        else:
            print('=')