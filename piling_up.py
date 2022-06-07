T = int(input())
for _ in range(T):
    n = int(input())
    T = list(map(int, input().split()))
    left = 0
    right = n - 1
    stack = 2 ** 31
    success_flag = True
    while left < right:
        if T[left] >= T[right]:
            if stack >= T[left]:
                stack = T[left]
                left += 1
            else:
                success_flag = False
                break
        else:
            if stack >= T[right]:
                stack = T[right]
                right -= 1
            else:
                success_flag = False
                break
    print('Yes' if success_flag else 'No')
