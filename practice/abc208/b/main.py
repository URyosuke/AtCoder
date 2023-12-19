#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


P = I()
# A = [LI() for _ in range(N)]
# 答えを格納する変数
ans=0

# i=10～0まで、-1ずつ
for i in range(10,0,-1):
    # i!円のコイン
    coin=math.factorial(i)

    # コインよりPが大きい間
    while coin<=P:
        # コインを使う
        ans+=1
        # 使った分をマイナス
        P-=coin
        
# 答えを出力
print(ans)