__author__ = 'Pascal'

out = open('result.txt', 'w')
with open('B-large.in') as f:
    case = 1
    f.readline()
    for line in f:
        n = list(line)
        try:
            n.remove('\n')
        except ValueError:
            pass
        last = n[0]
        c = 0
        print("Case #" + str(case))
        for i in range(1, len(n)):
            print(last)
            if last != n[i]:
                print("switch")
                last = n[i]
                c += 1
        print(last)
        if last == "-":
            c += 1
        out.write("Case #" + str(case) + ": " + str(c) + "\n")
        case += 1
out.close()
