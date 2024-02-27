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
from string import ascii_lowercase
N = SI()
S = SS()
Q = SI()
# 変換前と変換後の文字列を作る
# 'abcdefghijklmnopqrstuvwxyz' で初期化
mapping_from = ascii_lowercase
mapping_to = ascii_lowercase
for _ in range(Q):
    c, d = MS()
    mapping_to = mapping_to.replace(c, d) # c を d に置き換える
# 対応する文字をそれぞれ置き換える
print(S.translate(str.maketrans(mapping_from, mapping_to)))
        