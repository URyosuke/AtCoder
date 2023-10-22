N = list(map(int,input().split()))

if N[0] - N[1] == N[1] - N[2]:
    print('Yes')
elif N[0] - N[2] == N[2] - N[1]:
    print('Yes')
elif N[1] - N[0] == N[0] - N[2]:
    print('Yes')
elif N[1] - N[2] == N[2] - N[0]:
    print('Yes')
elif N[2] - N[0] == N[0] - N[1]:
    print('Yes')
elif N[2] - N[1] == N[1] - N[0]:
    print('Yes')
else:
    print('No')
    