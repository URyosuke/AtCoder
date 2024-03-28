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
N, X = MI()

dist=set()

# 最初は0にいる
dist.add(0)

# N回
for i in range(1,N+1):
    # 入力の受け取り
    a,b=map(int,input().split())

    # 新しい到達できる場所
    new_dist=set()

    # now=(i-1)回目のジャンプで到達できる場所
    for now in dist:
        # +aした場所がX以下なら
        if now+a<=X:
            # 新しい到達できる場所に記録
            new_dist.add(now+a)
        # +bした場所がX以下なら
        if now+b<=X:
            # 新しい到達できる場所に記録
            new_dist.add(now+b)

    # 到達できる場所を更新
    dist=new_dist

# Xがdistにあれば
if X in dist:
    # 「Yes」を出力
    print("Yes")
# そうでなければ(Xがdistになければ)
else:
    # 「No」出力
    print("No")

# def dfs(place, i):
#     if i == N and place == X:
#         print('Yes')
#         sys.exit()
#     elif i >= N:
#         return
#     else:
#         dfs(place + jump[i][0], i+1)
#         dfs(place + jump[i][1], i+1)

# dfs(0, 0)
# print('No')