# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
x, y = map(int, input().split())
P = list(input().split())
if P[0] != '-':
    P.insert(0, '+')
    
result = 0

for i in range(len(P) // 2):
    coeff = P[2 * i + 1].split('*')[-1]
    if P[2 * i] == '+':
        if coeff == 'x':
            result += x
        elif coeff == '1':
            result += 1
        else:
            result += x ** int(coeff)
    else:
        if coeff == 'x':
            result -= x
        elif coeff == '1':
            result -= 1
        else:
            result -= x ** int(coeff)
    
print(True if y == result else False)