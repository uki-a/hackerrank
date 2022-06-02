# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = -101
    second = -101
    for i in range(n):
        if first < arr[i]:
            second = first
            first = arr[i]
        elif second < arr[i] < first:
            second = arr[i]
    
    print(second)