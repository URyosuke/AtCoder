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
N = SI()
str_N = str(N)
ketasu = len(str_N)
mod = 998244353

def S(A,B):
    return (B-A+1)*(A+B)//2

ans = 0
# x~1~18
for x in range(1,19):
    # 10^x≤Nならば
    if 10**x<=N:
        # 「1~9*10**(x-1)までの和」
        ans+=S(1,9*10**(x-1))
        # 余りを取る
        ans%=mod
    # 10^(x-1)≤N<10^xならば
    else:
        # 「1～(N-10^(x-1)+1)までの和」
        ans+=S(1,N-10**(x-1)+1)
        # 余りを取る
        ans%=mod
        # forを抜ける
        break

# 答えの出力
print(ans)
    