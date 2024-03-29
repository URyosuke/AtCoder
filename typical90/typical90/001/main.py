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
N, L = MI()
K = SI()
A = LI()

def check(x):
    num = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= x:
            num += 1
            pre = A[i]
    if L - pre >= x:
        num += 1
    return (num >= K+1)

left, right = -1, L + 1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)