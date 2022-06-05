from collections import defaultdict
n = int(input())
s = defaultdict(int)
for _ in range(n):
    s[input()] += 1
    
print(len(s))

for num in s.values():
    print(num, end=' ')