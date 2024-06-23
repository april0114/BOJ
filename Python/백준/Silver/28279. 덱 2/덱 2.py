import sys
from collections import deque
N = int(sys.stdin.readline().strip())
d=deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == '1':
        d.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        d.append(int(cmd[1]))
    elif cmd[0] == '4':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif cmd[0] == '3':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif cmd[0] == '6':
        if d:
            print(0)
        else:
            print(1)
    elif cmd[0] == '5':
        print(len(d))
    elif cmd[0] == '7':
        if d:
            print(d[0])
        else:
            print(-1)
    elif cmd[0] == '8':
        if d:
            print(d[-1])
        else:
            print(-1)

