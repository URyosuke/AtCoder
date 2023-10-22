N = int(input());
A = list(map(int,input().split()));
M = int(input());
B = [0 for i in range(M)];

S = [0 for i in range(N)];
S[1] = 0;
ans = 0;
for i in range(1,N):
    S[i] = S[i-1] + A[i-1];
    
for i in range(M):
    B[i] = int(input());
    
for i in range(M-1):
    if B[i] > B[i+1]:
        ans += S[B[i] - 1] - S[B[i+1] -1];
    else:
        ans += S[B[i+1]-1] - S[B[i] - 1];
print(ans);
