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

def isCheckRiku(curr):
    if S[curr[0]][curr[1]] == '.':
        return True
    else:
        return False

H,W,N = MI()
T = SS()
S = [SS() for _ in range(H)]

is_final_place = numpy.full((H, W), False, dtype=bool)

for i in range(1,H-1):
    for j in range(1,W-1):
        curr = [i,j]
        flag = True
        if isCheckRiku(curr):
            for k in range(len(T)-1, -1, -1):
                move = T[k]
                if move == 'L':
                    curr = [curr[0],curr[1] + 1]
                    if isCheckRiku(curr):
                        continue
                    else:
                        flag = False
                        break
                elif move == 'R':
                    curr = [curr[0], curr[1] - 1]
                    if isCheckRiku(curr):
                        continue
                    else:
                        flag = False
                        break
                elif move == 'U':
                    curr = [curr[0]+1, curr[1]]
                    if isCheckRiku(curr):
                        continue
                    else:
                        flag = False
                        break
                elif move == 'D':
                    curr = [curr[0] - 1, curr[1]]
                    if isCheckRiku(curr):
                        continue
                    else:
                        flag = False
                        break
            if flag:
                is_final_place[i][j] = True
ans = 0
for i in range(H):
    for j in range(W):
        if is_final_place[i][j]:
            ans += 1
               
print(ans) 
