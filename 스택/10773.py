k = int(input()) #입력 받을 줄의 갯수
stack= [] #빈 리스트 생성

for i in range(k):#k번 만큼 돌아야 함
    a = int(input()) #k번 만큼 입력받을 정수 a
    if a!=0:
        stack.append(a) #a가 0 이 아닐 경우 a의 값 저장
    if a==0:
        stack.pop() #a 가 0일 경우 리스트 요소 한개 삭제
print(sum(stack)) #sum 함수 사용해서 값 더해주기
