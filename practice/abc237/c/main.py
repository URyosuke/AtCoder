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
S = SS()
S_list = list(S)
S_rev_list = list(reversed(S_list))
S_rev = ''.join(S_rev_list)

tail_a = 0
head_a = 0
for i in range(len(S)):
    if S[i] == 'a':
        head_a += 1
    else:
        break

for i in range(len(S_rev)):
    if S_rev[i] == 'a':
        tail_a += 1
    else:
        break

if head_a > tail_a:
    print('No')
    sys.exit()

S = 'a'*(tail_a-head_a) + S
S_rev = S_rev + 'a'*(tail_a-head_a)

if S == S_rev:
    print('Yes')
else:
    print('No')
    