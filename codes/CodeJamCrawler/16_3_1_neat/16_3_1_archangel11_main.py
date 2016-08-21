filename = "a.in"
outfilename = "output.txt"

def solve(f):
    n = int(f.readline())
    arr = map(int, f.readline().split())
    a = 'A'
    senate = []
    for i in range(n):
        senate.append([arr[i], chr(ord('A') + i)])

    ans = []
    while senate:
        senate = list(reversed(sorted(senate)))
        if ((len(senate) == 2 and senate[0][0] == senate[1][0]) or
            (len(senate) > 2 and senate[1][0] > senate[2][0])):
            ans.append(senate[0][1] + senate[1][1])
            senate[0][0] -= 1
            senate[1][0] -= 1
        else:
            ans.append(senate[0][1])
            senate[0][0] -= 1

        newSenate = []
        for num, char in senate:
            if num > 0:
                newSenate.append([num, char])
        senate = newSenate


    return " ".join(ans)

def out(s, o):
    print s
    o.write("{}\n".format(s))

def main():
    f = open(filename)
    o = open(outfilename, 'w+')
    T = int(f.readline())
    t = 1
    while t <= T:
        output = solve(f)
        out("Case #{}: {}".format(t, output), o)
        t+=1

if __name__ == "__main__":
    main()
