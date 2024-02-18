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
taka = [LI() for _ in range(M)]
aoki = [LI() for _ in range(M)]
for i in range(M):
    taka[i].sort
sorted_taka = sorted(taka, key=lambda x:(x[0], x[1]))

perm = [i+1 for i in range(N)]
pat = (list(itertools.permutations(perm)))
for aoki_shuffle in pat:
    new_aoki = [[0, 0] for i in range(M)]
    for i in range(M):
        new_aoki[i][0] = aoki_shuffle.index(aoki[i][0]) + 1
        new_aoki[i][1] = aoki_shuffle.index(aoki[i][1]) + 1
        if new_aoki[i][0] > new_aoki[i][1]:
            new_aoki[i][0], new_aoki[i][1] = new_aoki[i][1], new_aoki[i][0]
    sorted_aoki = sorted(new_aoki,key=lambda x:(x[0], x[1]))
    if sorted_taka == sorted_aoki:
        print('Yes')
        sys.exit()
print('No')