def solve(grid,m):
    counts = {}
    suspects = []
    for line in grid:
        for n in line:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
    for n in counts:
        if counts[n] % 2 == 1:
            suspects.append(n)
    if len(suspects) == m:
        return(' '.join(map(str,sorted(suspects))))
    else:
        return("ERROR")
def main():
    n_cases = int(input())
    for case in range(1,n_cases+1):
        m = int(input())
        lines = []
        for i in range(2*m - 1):
            line = input().split()
            line = list(map(int,line))
            lines.append(line)
        s = solve(sorted(lines),m)
        print("Case #{}: {}".format(case,s))
        # if len(s) == 1:
        #     print("Case #{}: {}".format(case,' '.join(map(str,s[0]))))
        # else:
        #     print("ERROR")
        #     print(sorted(lines))
        #     print(s)
        #     break

if __name__ == '__main__':
    main()
