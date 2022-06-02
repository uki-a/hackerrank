#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    name_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score.append([name, score])
    
    second_lowest_score = sorted(list(set([s for n, s in name_score])))[1]
    
    lowest_names = []
    
    for n, s in name_score:
        if s == second_lowest_score:
            lowest_names.append(n)
            
    for n in sorted(lowest_names):
        print(n)