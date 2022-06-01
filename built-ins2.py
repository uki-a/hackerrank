#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    
    answer = ""
    
    for i in range(1, n + 1):
        answer += str(i)
    
    print(answer)