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
N,Q = MI()
A = LI()
A.sort()
# 二分探索
# 引数：x　返り値：身長がx以上の生徒の人数
def Nibutan(x):
    # x≤A[0](最も小さいAの要素)ならば
    if x<=A[0]:
        # N人
        return N
    # A[N-1](最も大きいAの要素)<xならば
    elif A[N-1]<x:
        # 0人
        return 0
    # 左端(常にA[left]<x)
    left=0
    # 右端(常にx≤A[right])
    right=N-1

    # 1<右端-左端の間
    while 1<right-left:
        # 真ん中
        center=(left+right)//2
        # もしA[center]<xならば
        if A[center]<x:
            # 左端を真ん中へ更新
            left=center
        # そうでなければ(x≤A[center])
        else:
            # 右端を真ん中へ更新
            right=center
        
    # (N-右端)人
    return N-right

# Q回
for i in range(Q):
    # 入力の受け取り
    x=int(input())
    # 答えの出力
    print(Nibutan(x))


# for i in range(Q):
#     x = SI()
#     if i == 0:
#         left = 0
#         right = N
#     while left <= right-1:
#         # 1/2の人に聞く
#         mid = math.ceil((right-left)//2)
#         if x < A[mid]:
#             right = mid-1
#         else:
#             left = mid
#     # 長さが2になったら
#     if A[left] <= x:
#         idx = left
#     else:
#         idx = right
#     print(len(A[idx:]))