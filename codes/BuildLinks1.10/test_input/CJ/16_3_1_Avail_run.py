import sys
from collections import OrderedDict
from sortedcontainers import SortedDict
from string import ascii_uppercase

def main(infile, outfile):
    NUMS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    with open(infile) as inf:
        with open(outfile, 'w') as outf:
            test_case = 1
            case_count = int(inf.readline())
            while test_case <= case_count:
                
                order = []
                p_n = int(inf.readline())
                party_sizes = {ascii_uppercase[i]: int(x) for i,x in enumerate(inf.readline().split())}
                print(party_sizes)
                d = OrderedDict(sorted(party_sizes.items(), key=lambda t: t[1], reverse=True))
                size = 0
                for k,v in d.items():
                    size += v

                while len(d) > 0:
                    l = list(d.items())
                    f = l[0]
                    try:
                        s = l[1]
                    except IndexError:
                        s = ('-', 0)
                    try:
                        t = l[2]
                    except IndexError:
                        t = ('-', 0)

                    if size == 3:
                        order.append(f[0])
                        party_sizes[f[0]] -= 1 
                        size -= 1
                    elif f[1] > s[1] +1:
                        order.append((f[0] * 2))
                        party_sizes[f[0]] -= 2
                        size -= 2
                    elif f[1] == s[1]:
                        order.append((f[0]+s[0]))
                        party_sizes[f[0]] -= 1
                        party_sizes[s[0]] -= 1
                        size -= 2
                    else:
                        order.append(f[0])
                        party_sizes[f[0]] -= 1 
                        size -= 1

                    for k in d.keys():
                        if party_sizes[k] == 0:
                            del party_sizes[k]

                    d = OrderedDict(sorted(party_sizes.items(), key=lambda t: t[1], reverse=True))
                    print(order, f, s)


                # Output
                t = "Case #{}: {}".format(test_case, ' '.join(order))
                print(t)
                outf.write(t)

                if test_case != case_count:
                    outf.write('\n')
                test_case += 1


if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    main(infile, outfile)
