# https://www.hackerrank.com/challenges/ginorts/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&isFullScreen=true&h_r=next-challenge&h_v=zen
arr = input()
lower = []
upper = []
odd = []
even = []

for i in range(len(arr)):
    if arr[i].isdigit():
        if int(arr[i]) % 2 == 1:
            odd.append(arr[i])
        else:
            even.append(arr[i])
    elif arr[i].islower():
        lower.append(arr[i])
    elif arr[i].isupper():
        upper.append(arr[i])
        
lower.sort()
upper.sort()
odd.sort()
even.sort()

print(''.join(lower) + ''.join(upper) + ''.join(odd) + ''.join(even))