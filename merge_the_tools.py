def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    previous = '0'
    ans = [[] for _ in range(n // k)]
    for i in range(n // k):
        s = set()
        for j in range(k):
            if string[i * k + j] not in s:
                ans[i].append(string[i * k + j])
                s.add(string[i * k + j])
            
    for i in range(n // k):
        print(''.join(ans[i]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)