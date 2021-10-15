import sys

n, m  = input().strip().split()
arr = list(map(int, input().strip().split()))
set_a = set(map(int, input().strip().split()))
set_b = set(map(int, input().strip().split()))

hap_a = filter(lambda r: r in set_a, arr)
hap_b = filter(lambda r : r in set_b, arr)
value = len(list(hap_a)) - len(list(hap_b))
print(value)
