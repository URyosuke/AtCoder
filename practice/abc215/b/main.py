#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()                         #一つの数字
# A,B = MI()                      #空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# A = LI()                        #シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    #N行の数字列を二次元配列に

for i in range(999):
    if N < 2**i:
        print(i-1)
        exit()
## WA
# 少数の丸め誤差が出るらしい
# ans = math.floor(math.log2(N))
# print(ans)