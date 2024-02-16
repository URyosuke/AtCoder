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
# 入力の受け取り
N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())

# 1つ目の操作：Kの下限
k1_left=max(1-A,1-B)
# 1つ目の操作：Kの上限
k1_right=min(N-A,N-B)

# 2つ目の操作：kの下限
k2_left=max(1-A,B-N)
# 2つ目の操作：kの上限
k2_right=min(N-A,B-1)

# 左上の(行,列)
leftup_gyou,leftup_retu=A+k1_left,B+k1_left
# 右下の(行,列)
rightlow_gyou,rightlow_retu=A+k1_right,B+k1_right
# 右上の(行,列)
rightup_gyou,rightup_retu=A+k2_left,B-k2_left
# 左下の(行,列)
leftlow_gyou,leftlow_retu=A+k2_right,B-k2_right

# 答え：最初は全てのマスが白
# 0インデックスのため「S-R+1」+1,「Q-P+1」+1とする
ans=[["."]*(S-R+1+1) for i in range(Q-P+1+1)]

# 行：i
for i in range(P,Q+1):
    # 列：j
    for j in range(R,S+1):
        # 左上～右下の範囲にあるかチェック
        if leftup_gyou<=i<=rightlow_gyou and leftup_retu<=j<=rightlow_retu:
            # 黒マスかどうかのチェック
            if i-leftup_gyou==j-leftup_retu:
                # 黒に塗る
                ans[i-P+1][j-R+1]="#"
        # 右上～左下の範囲にあるかチェック
        if rightup_gyou<=i<=leftlow_gyou and leftlow_retu<=j<=rightup_retu:
            # 黒マスかどうかのチェック
            if leftlow_gyou-i==j-leftlow_retu:
                # 黒に塗る
                ans[i-P+1][j-R+1]="#"

# 行=1~((Q-P+1+1)-1)まで
for gyou in range(1,Q-P+1+1):
    # gyou行目の情報
    ans_gyou=""
    # 列=1~((S-R+1+1)-1)まで
    for retu in range(1,S-R+1+1):
        # 一列ずつ黒か白か確認
        ans_gyou+=ans[gyou][retu]
    # 出力
    print(ans_gyou)