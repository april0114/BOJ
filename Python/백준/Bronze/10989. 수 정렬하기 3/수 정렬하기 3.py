import sys
a = int(sys.stdin.readline())
num = [0] * 10001

for _ in range(a):
    ## 배열안 입력 받을 숫자
    b = int(sys.stdin.readline())
    ## 배열 안 숫자 확인 후 증가
    num[b] += 1

for i in range(10001):
    if num[i]:
        for j in range(num[i]):
            print(i)