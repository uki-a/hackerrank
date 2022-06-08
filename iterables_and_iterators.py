from itertools import combinations

N = int(input())
arr = list(input().split())
K = int(input())

count = 0
total = 0

for c in combinations(arr, K):
    if 'a' in c:
        count += 1
    total += 1

print(count / total)