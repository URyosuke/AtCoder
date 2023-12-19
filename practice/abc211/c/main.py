#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

#文字列を受け取り、最初の文字は?にする
S = S()
N = len(S)
S = "?" + S

#対象の文字列も同様に最初の文字を？にする
T = "?chokudai"

mod = 10**9+7

#dpの表を作るための二次元配列
dp = [[0]*9 for i in range(N+1)]

for i in range(9):
    dp[0][i] = 0
for i in range(N+1):
    dp[i][0] = 1

for i in range(1,N+1):
    for j in range(1,9):
        if S[i] == T[j]:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j]
    dp[i][j] %= mod

print(dp[N][8])