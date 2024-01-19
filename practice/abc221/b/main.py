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

S = SS()
T = SS()

# S,Tが一致していれば
if S==T:
    # Yesを出力
    print("Yes")
    # 終了
    exit()
    
S_list=list(S)
T_list=list(T)

# i=0~(Sの文字数-1)まで
for i in range(len(S)-1):
    # i文字目,i+1文字目とi+1文字目,i文字目を交換
    S_list[i],S_list[i+1]=S_list[i+1],S_list[i]
    # S_listとT_listが一致していれば
    if S_list==T_list:
        # Yesを出力
        print("Yes")
        # 終了
        exit()
    # 交換したものをもとに戻す
    S_list[i],S_list[i+1]=S_list[i+1],S_list[i]
    
# 一致しないままforを抜けたらNoを出力
print("No")
