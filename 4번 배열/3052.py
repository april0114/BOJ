a = []

for _ in range(10):
  b = int(input())
  c = b % 42
  a.append(c)    //append= 추가

s = set(a)       //set = 중복요소 제거해줌
print(len(s))    // list안에 갯수 세줌
