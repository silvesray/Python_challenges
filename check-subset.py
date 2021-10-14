import sys
from functools import reduce
# Enter your code here. Read input from STDIN. Print output to STDOUT
arr = []
for i, line in enumerate(sys.stdin):
    if i == 0:
        pass
    else:
        if i %2 == 0:
            arr.append(set(map(int, line.strip().split())))
            if len(arr) == 2:
                value = reduce(lambda r,s: r-s, arr)
                value = True if  len(value) == 0 else False
                print(value)
                arr.clear()
        else:
            pass
