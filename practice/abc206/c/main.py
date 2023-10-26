#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()

# defaultdictのインポート
# 要素の出現回数を数える連想配列countを用意
count=collections.defaultdict(int)

# Aのそれぞれの要素(a)について
for a in A:
    # aの出現回数を+1
    count[a]+=1

# 全組み合わせ=N*(N-1)//2
ans=N*(N-1)//2

# countの値(x)それぞれについて
for x in count.values():
    # Ai=Ajとなる組の数x*(x-1)//2を引く
    ans-=x*(x-1)//2

# 答えの出力
print(ans)