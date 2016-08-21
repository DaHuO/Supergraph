import sys

in_name = sys.argv[0]
f = sys.stdin
c = f.readline()
count = 1
for n in f:
    arr = {}
    n = int(n)
    for i in range(1, 10**6):
        for c in str(n * i):
            arr[c] = True
        if len(arr) == 10:
            print "Case #{0}: {1}".format(count, n * i)
            break
    else:
        print "Case #{0}: INSOMNIA".format(count)
    count += 1
