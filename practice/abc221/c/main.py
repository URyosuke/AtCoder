#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def SI(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def MS(): return map(str, sys.stdin.readline().rstrip().split())
def LS(): return list(sys.stdin.readline().rstrip().split())

N = SS()                         # 一つの数字
# A,B = MI()                      # 空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# S = MS()                        # 複数の文字列を空白区切りで与えられた時
# A = LI()                        # シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    # N行の数字列を二次元配列に

ans = 0
# 1<<len(N): 100...00 (0の数がN個)
for bitnum in range(1<<len(N)):
    A = []
    B = []
    
    for shift in range(len(N)):
        if bitnum >> shift & 1 == 0:
            A.append(N[shift])
        else:
            B.append(N[shift])
    
    if A == [] or B == []:
        continue
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    A_join = "".join(A)
    B_join = "".join(B)
    
    tmp_ans = int(A_join) * int(B_join)
    ans = max(ans, tmp_ans)

print(ans)