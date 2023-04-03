N = int(input())
a = input() #문자열로 입력받기

sum = 0

for i in a:
  sum += int(i) #문자열로 입력 받은 숫자를 한글자씩 정수형으로 변경
print(sum)
