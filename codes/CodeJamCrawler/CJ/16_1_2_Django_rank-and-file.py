import sys

with open(sys.argv[1], 'r') as f:
    test_cases = int(f.readline())#ignore number o test cases

    for case in range (1, test_cases + 1):
        n = int(f.readline())
        lines = (2 * n) - 1
        #array = []
        merged = []
        for i in range(lines):
            line = f.readline()
            l = [int(x) for x in line.split()]
            #array.append(l)
            merged = merged + l

        #array = sorted(array, key=lambda a: a[0])

        odd_occurences = list(set([x for x in merged if merged.count(x) % 2 > 0]))
        odd_occurences.sort()
        odd_occurences = [str(x) for x in odd_occurences]
        
        print("Case #%d: %s" % (case, " ".join(odd_occurences)))
