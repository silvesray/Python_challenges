import sys
import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
orders = []
lines = iter(sys.stdin)

while True:
    try:
        element = next(lines).strip()
        orders.append([element])
    except StopIteration:
        break

i, N, p = 0, len(orders), 0
 
while i >= 0 and i < N :
    value = orders[i][0]
    checker = re.search("[a-z_]+", value)
    if i in (0, 2):
        if checker == None:
            pass
    else:
        if i == 1:
            arr = set(map(int, value.split()))
        else:
            if checker != None:
                p = value.split()
                if p[0] == "intersection_update":
                    p = i + 1
                    tmp = set(map(int, orders[p][0].split()))
                    arr &= tmp
                    
                elif p[0] == "update":
                    p = i + 1
                    tmp = set(map(int, orders[p][0].split()))
                    arr |= tmp
                    
                elif p[0] == "symmetric_difference_update":
                    p = i + 1
                    tmp = set(map(int, orders[p][0].split()))
                    arr ^= tmp
                    
                elif p[0] == "difference_update":
                    p = i + 1
                    tmp = set(map(int, orders[p][0].split()))
                    arr -= tmp
            else:
                pass
    
    i += 1
    
print(sum(arr))
    
