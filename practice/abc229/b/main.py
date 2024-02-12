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
A,B = MI()
length = 0

# 長い方の桁数探索すつために長さ取得
str_A = str(A)
str_B = str(B)
if A < B:
    length = len(str_A)
else:
    length = len(str_B)

for i in range(1,length+1):
    cur_A = int(str_A[-i])
    cur_B = int(str_B[-i])
    if cur_A + cur_B >= 10:
        print('Hard')
        sys.exit()
print('Easy')
    