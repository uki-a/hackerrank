# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# format と evel が便利だった
len_A = int(input())
A = set(map(int, input().split()))
n_query = int(input())
for _ in range(n_query):
    instruction, n = input().split()
    B = set(map(int, input().split()))
    n = int(n)
    eval('A.{}(B)'.format(instruction, ))
    
print(sum(list(A)))