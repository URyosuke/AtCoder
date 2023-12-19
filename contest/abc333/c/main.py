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

ls = [1,1,1]
lapu = ['', '', '']
 
curr = 0
for i in range(N-1):
    if i == 0:
        ls[0] += 1
        continue
    if ls[0] == ls[1] and ls[1] == ls[2]:
        ls[1] = 1
        ls[2] = 1
        ls[0] += 1
        continue
    if ls[0] != ls[1]:
        if ls[2] < ls[1]:
            ls[2] += 1
        else:
            ls[1] += 1
            ls[2] = 1
    else:
        ls[2] += 1

for i in range(3):
    for j in range(ls[i]):
        lapu[i] += '1'

ans = int(lapu[0]) + int(lapu[1]) + int(lapu[2])
print(ans)


## 公式別解（高々13桁を全探索）
# N = int(input())
# L = 12
# r = [int("1" * (i + 1)) for i in range(L)]
# for i in range(L):
#     for j in range(i + 1):
#         for k in range(j + 1):
#             N -= 1
#             if N == 0:
#                 print(r[i] + r[j] + r[k])
    