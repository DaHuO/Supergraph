
with open('in.txt') as in_f, open('out.txt', 'w') as out_f:
    n = in_f.readline()
    case = 0
    for line in in_f.readlines():
        case += 1
        k = int(line)
        if k == 0:
            print("Case #{}: INSOMNIA".format(case), file=out_f)
        else:
            seen = set()
            i = 1
            while True:
                num = i * k
                for c in str(num):
                    seen.add(int(c))
                if len(seen) == 10:
                    print("Case #{}: {}".format(case, num), file=out_f)
                    break
                i += 1
