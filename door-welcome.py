import sys

lines = next(iter(sys.stdin))
N, M = map(int, lines.strip().split())

for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
    
print('WELCOME'.center(M, '-'))

for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))
