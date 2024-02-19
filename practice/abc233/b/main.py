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
L, R = MI()
S = SS()

# Sを一文字ずつリストへ展開
S_list=list(S)

# Sの0～(L-2)文字目
S_left=S_list[:L-1]
# Sの(L-1)～(R-1)文字目
S_center=S_list[L-1:R]
# SのR文字目～末尾
S_right=S_list[R:]

# 中央を反転
S_center=S_center[::-1]

# リストを結合
S=S_left+S_center+S_right

# 文字列へ結合
S_join="".join(S)

# 答えの出力
print(S_join)