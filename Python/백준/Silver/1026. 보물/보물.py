N = int(input())
S = 0
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()

for i in range(N):
    S += A[i] * B.pop(B.index(max(B)))

print(S)