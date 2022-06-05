S = input() + '\n'

previous = -1
cnt = 0

ans = []

for i in range(len(S)):
    if previous != S[i]:
        ans.append((cnt, int(previous)))
        previous = S[i]
        cnt = 1
    else:
        cnt += 1
    

for a in ans[1:]:
    print(a, end=' ')