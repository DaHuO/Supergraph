def rankFile(n, rows):
    d = {}
    for row in rows:
        for num in row:
            try:
                d[num]+=1
            except KeyError:
                d[num]=1
    odds = []
    for key,value in d.items():
        if value%2 == 1:
            odds.append(key)
    odds.sort()
    odds = [str(i) for i in odds]
    return " ".join(odds)

if __name__ == '__main__':
    T = int(input())
    for case in range(1,T+1):
        n = int(input())
        rows = []
        for i in range(2*n-1):
            rows.append([int(num) for num in input().split()])
        print("Case #{0}: {1}".format(case, rankFile(n,rows)))