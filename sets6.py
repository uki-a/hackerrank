# https://hr-testcases-us-east-1.s3.amazonaws.com/9456/input02.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1654254880&Signature=N%2BjWcsj4U6bkOYx8WmITM4m2Af8%3D&response-content-type=text%2Fplain
A = set(map(int, input().split()))
n = int(input())
ans = True
for _ in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B) and B != A:
        ans = False
    
print(ans)