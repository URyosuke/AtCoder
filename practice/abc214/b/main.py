#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

# N = I()                         #一つの数字
S,T = MI()                      #空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# A = LI()                        #シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    #N行の数字列を二次元配列に

ans = 0
for i in range(S+1):
    for j in range(S+1):
        for k in range(S+1):
            if i + j + k <= S:
                if i * j * k <= T:
                    ans += 1
print(ans)