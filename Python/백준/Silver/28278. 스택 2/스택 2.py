import sys
N = int(sys.stdin.readline())
lst =[]

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == '1':
        lst.append(int(cmd[1]))
    elif cmd[0] == '2':
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif cmd[0] == '3':
        print(len(lst))
    elif cmd[0] == '4':
        if lst:
            print(0)
        else:
            print(1)
    elif cmd[0] == '5':
        if lst:
            print(lst[-1])
        else:
            print(-1)