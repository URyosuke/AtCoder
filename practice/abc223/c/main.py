#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def SI(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(float, sys.stdin.readline().rstrip().split()))
def SS(): return sys.stdin.readline().rstrip()
def MS(): return map(str, sys.stdin.readline().rstrip().split())
def LS(): return list(sys.stdin.readline().rstrip().split())

N = SI()                         # 一つの数字
# A,B = MI()                      # 空白区切りで複数の数字が与えられ、それらを別々の変数に格納したい時
# S = MS()                        # 複数の文字列を空白区切りで与えられた時
# A = LI()                        # シンプルに数列一行を読み込む
# A = [LI() for _ in range(N)]    # N行の数字列を二次元配列に

line = [LI() for _ in range(N)]

burn_time=0
for i in range(N):
    burn_time+=line[i][0]/line[i][1]
# 両橋から燃やすから1/2
burn_time=burn_time/2
ans=0
for i in range(N):
    burn_time_N=line[i][0]/line[i][1]
    if burn_time<=burn_time_N:
        ans+=burn_time*line[i][1]
        break
    else:
        burn_time-=burn_time_N
        ans+=line[i][0]
        
print(ans)