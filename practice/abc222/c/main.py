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

N, M = MI()
A = [SS() for _ in range(2*N)]
wins = [[0,i] for i in range(2*N)]

# 勝った手を返す関数
def janken(a, b):
    # 引き分けなら-1,前者勝ちなら0,後者勝ちなら1
    if a == b: return -1
    elif a == 'G' and b=='P': return 1
    elif a=='C' and b=='G': return 1
    elif a=='P' and b=='C': return 1
    return 0
    
for i in range(M):
    for j in range(N):
        # 現在ランク順にプレイヤーIDをplayer1, player2に格納
        player1 = wins[2*j][1]
        player2 = wins[2*j+1][1]
        # じゃんけんの結果をresultに格納
        result = janken(A[player1][i], A[player2][i])
        # resultの結果があいこ以外の時は現時点で2*j+result番目の人のポイントを-1
        if result != -1: wins[2*j+result][0] -= 1
    wins.sort()
    
for _,i in wins: print(i+1)

        