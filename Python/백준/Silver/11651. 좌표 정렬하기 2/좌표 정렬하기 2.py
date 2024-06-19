import sys

#n개 입력받기
N = int(input())
#리스트 
arr = []
for i in range(N):
    x,y = map(int, input().split())
    arr.append([y,x])

sort_arr = sorted(arr)

for y,x in sort_arr:
    print(x,y)