#!/user/anaconda3/bin/python3
import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
Arr = [LI() for _ in range(3)]

count = 0
A_count = [0] * N
B_C = []
B_C_count = [0] * N

#B[Cj]を作る
for i in range(N):
    B_C.append(Arr[1][Arr[2][i] - 1])
    
#AのNまでの数をカウントし配列に格納
for i in range(N):
    A_count[Arr[0][i]-1] += 1

#BのNまでの数をカウントし配列に格納
for i in range(N):
    B_C_count[B_C[i]-1] += 1
    

for i in range(N):
    count += A_count[i] * B_C_count[i]
    

print(count)

