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
N,K = MI()
P = [LI() for _ in range(N)]
sumP = []

# それぞれ3日目までの合計点
for i in range(N):
    sumP.append([sum(P[i])])
    sumP[i].append(i)
sumP.sort(reverse=True)

# K位以内に入る可能性があるかどうか判定するリスト
is_pass = [False]*N
    
for i in range(N):
    if i == 0:
        is_pass[sumP[i][1]] = True
        continue
    if i+1 <= K:
        is_pass[sumP[i][1]] = True
        continue
    else:
        if (sumP[K-1][0] - sumP[i][0]) <= 300:
            is_pass[sumP[i][1]] = True

for i in range(N):
    if is_pass[i] == True:
        print('Yes')
    else:
        print('No')        
        