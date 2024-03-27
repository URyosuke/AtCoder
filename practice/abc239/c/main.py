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
# A,B = MI()                      # 空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# S = MS()                        # 複数の文字列を空白区切りで与えられた時
# A = LI()                        # シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    # N行の数字列を二次元配列に
x1, y1, x2, y2 = MI()
p = []

# 候補点を格納
p.append([x1+2,y1+1])
p.append([x1+2,y1-1])
p.append([x1-2,y1+1])
p.append([x1-2,y1-1])
p.append([x1+1,y1+2])
p.append([x1+1,y1-2])
p.append([x1-1,y1+2])
p.append([x1-1,y1-2])

for x3,y3 in p:
    if (x3-x2)**2 + (y3-y2)**2 == 5:
        print('Yes')
        sys.exit()
print('No')