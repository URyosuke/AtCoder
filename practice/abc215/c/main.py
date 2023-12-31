#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def SI(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def MS(): return map(str, sys.stdin.readline().rstrip().split())
def LS(): return list(sys.stdin.readline().rstrip().split())

# N = I()                         #一つの数字
# A,B = MI()                      #空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# A = LI()                        #シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    #N行の数字列を二次元配列に

S,K = MS()
K = int(K)

# 配列と違い、重複をなくせる
S_set = set()

# 引数として列挙可能なオブジェクトが必要
for seq in itertools.permutations(range(len(S))):
    S_tmp =""
    # 文字列を連結する
    for i in seq:
        S_tmp += S[i]
        
    # セットにっ格納
    S_set.add(S_tmp)

S_list = list(S_set)
S_list.sort()

print(S_list[K-1])

