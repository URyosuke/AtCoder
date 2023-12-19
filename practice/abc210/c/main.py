#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N,K = MI()
c = LI()

# defaultdictのインポート
from collections import defaultdict
# int:デフォルトの値を0にする
colors=defaultdict(int)

# 色の種類数を数える変数
cnt=0

# i=0~K-1まで
for i in range(K):
    # c[i]の個数をプラス1
    colors[c[i]]+=1
    # c[i]の個数が0→1になったら
    if colors[c[i]]==1:
        # 色の種類数プラス1
        cnt+=1

# 答え　暫定答えをcntとする
ans=cnt

# i=1~N-Kまで
for i in range(1,N-K+1):
    # c[i-1]の個数をマイナス1
    colors[c[i-1]]-=1
    # c[i-1]の個数が1→0になったら
    if colors[c[i-1]]==0:
        # 色の種類数マイナス1
        cnt-=1
    # c[i+K-1]の個数をプラス1
    colors[c[i+K-1]]+=1
    # c[i+K-1]の個数が0→1になったら
    if colors[c[i+K-1]]==1:
        # 色の種類数プラス1
        cnt+=1
    # cntのほうが大きかったら答えを更新
    ans=max(ans,cnt)

# 答えの出力
print(ans)