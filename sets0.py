#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n_english = int(input())
set_english = set(list(map(int, input().split())))
n_french = int(input())
set_french = set(list(map(int, input().split())))

print(len(set_english & set_french))