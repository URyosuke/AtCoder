#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def St(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

# N = I()                         #一つの数字
S = St()                      #空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
T = St()                      #空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# A = LI()                        #シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    #N行の数字列を二次元配列に

pata = dict()
pata["A"] = 1
pata["B"] = 2
pata["C"] = 3
pata["D"] = 4
pata["E"] = 5

S1Num = pata[S[0]]
S2Num = pata[S[1]]
T1Num = pata[T[0]]
T2Num = pata[T[1]]

SDis = abs(S1Num - S2Num)
TDis = abs(T1Num - T2Num)

if (S1Num == 1 and S2Num == 5) or (S1Num == 5 and S2Num == 1):
    SDis = 1
if (T1Num == 1 and T2Num == 5) or (T1Num == 5 and T2Num == 1):
    TDis = 1

if SDis == TDis:
    print('Yes')
elif (SDis == 2 and TDis == 3) or (SDis == 3 and TDis == 2):
    print('Yes')
else:
    print('No')