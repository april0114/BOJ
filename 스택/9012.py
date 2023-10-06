a = int(input()) #입력 받을 줄의 갯수

for _ in range(a): #입력받은 줄의 개수 만큼 돌 for문
    stack = [] #리스트 생성
    b = input()

    for c in b: #괄호를 확인해줄 for 문
        if c == '(':
            stack.append(c)
        elif c == ')':
          #존재할 경우
            if stack:
                stack.pop()
              #없을 경우
            else:
                print("NO")
                break
            
    else:        
        if len(stack) == 0:
            print("YES")
        else:
            print("NO") 
