#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def SI(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def MS(): return map(str, sys.stdin.readline().rstrip().split())
def LS(): return list(sys.stdin.readline().rstrip().split())

N = SI()  # 一つの数字
# A,B = MI()                      # 空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# S = MS()                        # 複数の文字列を空白区切りで与えられた時
# A = LI()                        # シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    # N行の数字列を二次元配列に
from collections import deque
que = deque()
T = [0]
A = [[0]]

# T, K, Aを分けて入力
for i in range(N):
    tmp = LI()
    T.append(tmp[0])
    K = tmp[1]
    if 0 < K:
        a_list = tmp[2:]
        A.append(a_list)
    else:
        A.append([-1])

# 習得する必要がある技
learn=[False]*(N+1)

learn[N] = True
que.append(N)

while 0<len(que):
    waza = que.popleft()
    for x in A[waza]:
        if x == -1:
            break
        if learn[x] == False:
            que.append(x)
            learn[x] = True

ans = 0

for i in range(1,N+1):
    if learn[i] == True:
        ans += T[i]
print(ans)