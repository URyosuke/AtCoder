#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def SI(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def MS(): return map(str, sys.stdin.readline().rstrip().split())
def LS(): return list(sys.stdin.readline().rstrip().split())

# N = SI()                         # 一つの数字
N, Q = MI()                      # 空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# S = MS()                        # 複数の文字列を空白区切りで与えられた時
# A = LI()                        # シンプルに数列一行を読み込む
# query = [MI() for _ in range(Q)]    # N行の数字列を二次元配列に
query = []
for i in range(Q):
    query.append(LS())
from collections import defaultdict

dragon = defaultdict()
for i in range(N):
    dragon[str(i+1)] = [i+1,0]
    
def movebody(dragon):
    currdragon = dragon.copy()
    
    for i in range(N-1,0,-1):
        dragon[str(i+1)][0] = dragon[str(i)][0]
        dragon[str(i+1)][1] = dragon[str(i)][1]
    
for i in range(Q):
    if query[i][0] == '1':
        if query[i][1] == 'R':
            movebody(dragon)
            dragon['1'][0] += 1
        elif query[i][1] == 'L':
            movebody(dragon)
            dragon['1'][0] -= 1
        elif query[i][1] == 'U':
            movebody(dragon)
            dragon['1'][1] += 1
        elif query[i][1] == 'D':
            movebody(dragon)
            dragon['1'][1] -= 1
    else:
        print(*dragon[query[i][1]])
