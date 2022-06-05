n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = 0

for a in arr:
    if a in A:
        ans += 1
        
    elif a in B:
        ans -= 1
        
print(ans)
