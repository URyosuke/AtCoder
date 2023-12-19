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
S = LI()                        #シンプルに数列一行を読み込む
T = LI()                        #シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    #N行の数字列を二次元配列に

# 1週目
for i in range(N):
    # 次のすぬけ君の番号。i=N-1のとき、次のすぬけ君の番号=Nではなく=0とするため%Nとする。
    next=(i+1)%N
    # 高橋君からもらうのが早いか、左隣のすぬけ君からもらうのが早いか
    T[next]=min(T[next], T[i] + S[i])

# 2周目
for i in range(N):
    # 次のすぬけ君の番号。i=N-1のとき、次のすぬけ君の番号=Nではなく=0とするため%Nとする。
    next=(i+1)%N
    # 高橋君からもらうのが早いか、左隣のすぬけ君からもらうのが早いか
    T[next]=min(T[next], T[i] + S[i])

#答えの出力
for ans in T:
  print(ans)
    
