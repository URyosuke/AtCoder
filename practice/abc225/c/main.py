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
B = [LI() for i in range(N)]

gyou = (B[0][0]-1) // 7
left = gyou*7 + 1
right = left + 6

# retu=0～(M-1)まで
for retu in range(M):
    # Aの左端～右端の間になければ
    if B[0][retu]<left or right<B[0][retu]:
        # 「No」を出力
        print("No")
        # 終了
        exit()

# retu=1～(M-1)まで
for retu in range(1,M):
    # 0行目i列目　が　0行目(i-1)列目+1　でなければ
    if B[0][retu]!=B[0][retu-1]+1:
        # 「No」を出力
        print("No")
        # 終了
        exit()

# (2)Bの1行目(上から2段目)以降は「上の段+7」となっているか
# gyou=1~(N-1)まで
for gyou in range(1,N):
    # retu=0～(M-1)まで    
    for retu in range(M):
        # 「上の段+7」になっていなければ
        if B[gyou][retu]!=B[gyou-1][retu]+7:
            # 「No」を出力
            print("No")
            # 終了
            exit()

# 「Yes」を出力
print("Yes")
