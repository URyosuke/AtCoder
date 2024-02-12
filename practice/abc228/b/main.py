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
N,X = MI()
A = LI()

from collections import deque
friends = [False]*N
que = deque()
que.append(A[X-1])
# 最初に知る人
friends[X-1] = True

while len(que) != 0:
    known = que.popleft()
    if friends[known-1] == False:
        friends[known-1] = True
        que.append(A[known-1])

count=0
for i in range(N):
    if friends[i] == True:
        count += 1
print(count)