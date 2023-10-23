pypy로 제출해야함
N = int(input())
C = []

for i in range(N):
    a = int(input())
    C.append(a)
C.sort()

for i in range(N):
    print(C[i])
