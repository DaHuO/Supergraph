fin = open('B-large.in')
lines = fin.readlines()
fin.close()

T = int(lines.pop(0))
fout = open('pancakes_out.txt','w')
for t in range(T):
    # count the discontinuities:
    S = lines[t].strip()
    n = 0
    for (a,b) in zip(S,S[1:]):
        if a != b:
            n += 1
    print(n, "discontinuities")
    if not ((S[0]=="+") ^ (n%2)):
        # if first pancake was upside down and we have flipped an even number of times,
        # or first pancake was right way up and we have flipped an odd number of times,
        # flip again
        n += 1
        print("and another flip")

    fout.write("Case #%d: %d\n" % (t+1, n))

fout.close()
