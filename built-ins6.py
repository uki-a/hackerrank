# https://www.hackerrank.com/challenges/any-or-all/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&isFullScreen=true
n = int(input())
arr = list(map(int, input().split()))
print(True if all([a > 0 for a in arr]) and any([str(a) == str(a)[::-1] for a in arr]) else False)