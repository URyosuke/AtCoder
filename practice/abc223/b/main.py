#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def SI(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def MS(): return map(str, sys.stdin.readline().rstrip().split())
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
# N = SI()                         # 一つの数字
# A,B = MI()                      # 空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# S = MS()                        # 複数の文字列を空白区切りで与えられた時
# A = LI()                        # シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    # N行の数字列を二次元配列に

S=SS()
S = list(S)
S = deque(S)

ans_mini=''
ans_max=''

if len(S)==1:
    mojiS = ''.join(list(S))
    print(mojiS)
    print(mojiS)
    sys.exit()

for i in range(len(S)):
    if i==0:
        mojiS = ''.join(list(S))
        ans_mini=mojiS
        ans_max=mojiS
    S.rotate()
    mojiS = ''.join(list(S))
    if ans_mini > mojiS:
        ans_mini = mojiS
    if ans_max < mojiS:
        ans_max = mojiS

print(ans_mini)
print(ans_max)