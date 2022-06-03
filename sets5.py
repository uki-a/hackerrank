# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n_query = int(input())
for _ in range(n_query):
    n_a = int(input())
    A = set(map(int, input().split()))
    n_b = int(input())
    B = set(map(int, input().split()))
    
    if A.issubset(B):
        print(True)
    else:
        print(False)