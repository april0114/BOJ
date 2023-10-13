A = int(input())  #입력받을 갯수
c = [] #대기줄
num = 1
b =list(map(int,input().split())) #입력 받는 숫자

while b:
    if b[0] == num:
        b.pop(0)
        num += 1
    else :
        c.append(b.pop(0))
    while c:
        if c[-1] == num:
            c.pop()
            num +=1
        else:
            break

if not c:
    print("Nice")
else:
    print("Sad")
    
