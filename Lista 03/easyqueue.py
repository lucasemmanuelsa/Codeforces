import sys
from collections import deque

t = int(sys.stdin.readline())


queue = deque()

for i in range(t):
    entrada = sys.stdin.readline().split()
    if(entrada[0] == '1'):
        queue.append(int(entrada[1]))
    elif(entrada[0] == '2'):
        if(queue):
            queue.popleft()
    elif entrada[0] == '3':
        if(queue):
            sys.stdout.write(f'{queue[0]}\n')
        else:
            sys.stdout.write(f'Empty!\n')