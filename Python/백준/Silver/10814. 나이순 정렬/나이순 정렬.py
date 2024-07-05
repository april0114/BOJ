import sys

N = int(sys.stdin.readline())

diction = []
for i in range(N):
    a,b = input().split()
    a = int(a)
    diction.append((a,b))

diction.sort(key=lambda x: x[0])
for key,value in diction:
    print(key, value, sep=" ")
