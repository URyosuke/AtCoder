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

H,W=MI()
A=[LI() for _ in range(H)]

flag = 0
for i_1 in range(H-1):
    for i_2  in range(i_1+1,H):
        for j_1 in range(W-1):
            for j_2 in range(j_1+1,W):
                if A[i_1][j_1] + A[i_2][j_2] <= A[i_2][j_1] + A[i_1][j_2]:
                    flag = 1
                else:
                    print('No')
                    sys.exit()
print('Yes')
