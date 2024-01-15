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

X = SS()
N = SI()
S = []
for i in range(N):
    S_tmp = SS()
    S.append(S_tmp)

conv_letter = dict()
inv_letter = dict()

for i in range(len(X)):
    # X[0]が、例えば'b'のとき、conv_letter['b'] = a
    conv_letter[X[i]] = chr(i + 97)
    inv_letter[chr(i + 97)] = X[i]

# Sを通常のアルファベット順に変換する関数
def conv_name(S):
    result = ''
    for i in range(len(S)):
        result += conv_letter[S[i]]
    return result

# Sを新しいアルファベットに戻す関数
def inv_name(S):
    result = ''
    for i in S:
        result += inv_letter[i]
    return result

conv_names = []

for i in range(N):
    conv_names.append(conv_name(S[i]))

conv_names.sort()

for conv_S in conv_names:
    inv_S = inv_name(conv_S)
    print(inv_S)
    
