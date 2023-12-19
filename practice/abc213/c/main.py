#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


H,W,N = MI()
cards = []
gyou = []
retu = []

for i in range(N):
    A,B = MI()
    cards.append([A, B])
    gyou.append(A)
    retu.append(B)
    
## set()は集合、つまり重複をなくす
gyou = set(gyou)
gyou = list(gyou)
gyou.sort()

gyou_conv = dict()

for i in range(len(gyou)):
    gyou_conv[gyou[i]] = i + 1

#列も同じことをする
retu=set(retu)
retu=list(retu)
retu.sort()

retu_conv=dict()

for i in range(len(retu)):
    retu_conv[retu[i]]=i+1

# それぞれのカードについて行、列番号を変換して出力
for gyou,retu in cards:
    # 行の変換
    ans_gyou=gyou_conv[gyou]
    # れつの変換
    ans_retu=retu_conv[retu]
    # 答えを出力する
    print(ans_gyou,ans_retu)
