from itertools import combinations
from functools import reduce

n = int(input().strip())
line = input().strip().split()

data = {}
for i, e in enumerate(line, start=1):
    if e not in data:
        data[e] = [i]
    else:
        data[e] += [i]
        
k = int(input().strip())
indexes = reduce(lambda r,s : r+s, list(data.values()))

if 'a' not in data:
    print("{0}".format(0.000000000000))
else:
    perms = list(combinations(indexes, k))
    find_a = filter(lambda r : any([f in data["a"] for f in r]) , perms)
    ratio = len(list(find_a))/len(perms)
    print(ratio)
