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
N, A, B = MI()
D = LI()
right = 0

for i in range(1,N):
    if abs(D[0]-D[i]) < A:
        right = max(right, abs(D[0]-D[i]))
        continue
    else:
        buf = A-right
        if ((buf + abs(D[0]-D[i])) % (A+B)) <= A:
            right = max(right, (buf + abs(D[0]-D[i])) % (A+B) - buf)
            continue
        else:
            print('No')
            sys.exit()

print('Yes')