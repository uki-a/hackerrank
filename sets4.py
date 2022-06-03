# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
k = int(input())
arr = list(map(int, input().split()))

dict_count = {}

for a in arr:
    if a not in dict_count:
        dict_count[a] = 1
    else:
        dict_count[a] += 1

for d, c in dict_count.items():
    if c == 1:
        print(d)
        