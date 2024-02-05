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

N=SI()
points = [LI() for _ in range(N)]
count = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if points[k][0] == points[i][0]:
                lean_1 = float('inf') # 無限大を表す値に設定
            else:
                lean_1 = (points[k][1] - points[i][1]) * (points[k][0] - points[j][0])
            if points[k][0] == points[j][0]:
                lean_2 = float('inf') # 無限大を表す値に設定
            else:
                lean_2 = (points[k][1] - points[j][1]) * (points[k][0] - points[i][0])
            if lean_1 == lean_2:
                continue
            else:
                count += 1
print(count)
