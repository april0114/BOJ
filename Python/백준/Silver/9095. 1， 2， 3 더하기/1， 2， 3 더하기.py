import sys

T = int(sys.stdin.readline())
d=[0]*11
d[1]=1
d[2]=2
d[3]=4

for i in range(4,11):
    d[i]=d[i-3]+d[i-2]+d[i-1]

for _ in range(T):
    n = int(sys.stdin.readline())
    print(d[n])
