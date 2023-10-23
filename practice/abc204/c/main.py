#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,numpy,string;
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,M = LI()
A = [LI() for _ in range(M)]

connect = [[] for i in range(N + 1)]

# A[i][0]の都市から行ける都市をappend
# 都市1から都市2,3,4にいけるならconnect[1]=2,3,4
for i in range(M):
    connect[A[i][0]].append(A[i][1])

from collections import deque

def BFS(start_city):
    count = 1
    
    visited = [[False] for _ in range(N + 1)]
    visited[start_city] = True
    
    que = deque()
    que.append(start_city)
    
    while len(que) > 0:
        now_city = que.popleft()
        for to_city in connect[now_city]:
            if visited[to_city] != True:
                count += 1
                visited[to_city] = True
                que.append(to_city)
    return count

ans = 0
for city in range(1,N+1):
    ans += BFS(city)
print(ans)    
    