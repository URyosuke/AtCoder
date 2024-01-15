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
    
# #の数を数える関数
def countSharpe(X):
    count = 0
    for i in range(N):
        for j in range(N):
            if X[i][j] == '#':
                count += 1
    return count

# 90度回転させる関数
def rotate(X):
    rotate_X = [['.'] * N for i in range(N)]
    for gyou in range(N):
        for retsu in range(N):
            rotate_X[retsu][N-1-gyou] = X[gyou][retsu]
    return rotate_X

# 左上から始めて、始めて'#'が出てくるインデックスを返す関数
def firstSharp(X):
    for gyou in range(N):
        for retsu in range(N):
            if X[gyou][retsu] == '#':
                return gyou, retsu

# 下方向へmove_gyou,右方向へmove_retsu平行移動する関数
def translation(X, move_gyou, move_retsu):
    move_X = [['.'] * N for i in range(N)]
    for gyou in range(N):
        for retsu in range(N):
            # 行番号+move_gyou,列番号+move_retuがグリッドの中にあれば
            if 0<=gyou+move_gyou<N and 0<=retsu+move_retsu<N:
                # (行番号,列番号)→(行番号+move_gyou,列番号+move_retu)
                move_X[gyou+move_gyou][retsu+move_retsu]=X[gyou][retsu]
    return move_X

# S, Tが一致しているか確認する関数
def check(S, T):
    for gyou in range(N):
        for retsu in range(N):
            if S[gyou][retsu] != T[gyou][retsu]:
                return False
    return True

N = SI()
S = []
T = []

for i in range(N):
    S_temp = SS()
    # S_temp = list(S_temp)
    S.append(S_temp)
for i in range(N):
    T_temp = SS()
    # T_temp = list(T_temp)
    T.append(T_temp)

# '#'の数が違う場合
if countSharpe(S) != countSharpe(T):
    print('No')
    sys.exit()

for i in range(4):
    # 最初に回転する
    S = rotate(S)
    # 最初に'#'が出てくるインデックスを取得
    S_first_gyou, S_first_retsu = firstSharp(S)
    T_first_gyou, T_first_retsu = firstSharp(T)
    # 並行移動
    move_gyou = T_first_gyou - S_first_gyou
    move_retsu = T_first_retsu - S_first_retsu
    S_trans = translation(S, move_gyou, move_retsu)
    
    if check(S_trans, T):
        print('Yes')
        exit()
print('No')