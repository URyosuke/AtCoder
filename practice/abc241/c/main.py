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
N = SI()
S = [SS() for _ in range(N)]


def search_right(gyou, retu):
    count = 0
    for i in range(6):
        if S[gyou][retu+i] == '#':
            count += 1
    if count >= 4:
        return True
    else:
        False


def search_down(gyou, retu):
    count = 0
    for i in range(6):
        if S[gyou+i][retu] == '#':
            count += 1
    if count >= 4:
        return True
    else:
        return False


def search_right_down(gyou, retu):
    count = 0
    for i in range(6):
        if S[gyou+i][retu+i] == '#':
            count += 1
    if count >= 4:
        return True
    else:
        return False
    

def search_left_down(gyou, retu):
    count = 0
    for i in range(6):
        if S[gyou+i][retu-i] == '#':
            count += 1
    if count >= 4:
        return True
    else:
        return False


for gyou in range(N):
    for retu in range(N):
        if retu+5 < N:
            if search_right(gyou, retu):
                print('Yes')
                exit()
        if gyou+5 < N:
            if search_down(gyou, retu):
                print('Yes')
                exit()
        if retu+5 < N and gyou+5 < N:
            if search_right_down(gyou, retu):
                print('Yes')
                exit()
        if 0 <= retu-5 and gyou+5 < N:
            if search_left_down(gyou, retu):
                print('Yes')
                exit()
print('No')