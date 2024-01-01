a = int(input())
b = 0 #봉지수

while a>=0:
    if a % 5==0:
        b += (a//5)
        print(b)
        break
    a -=3
    b +=1

else:
    print(-1)
