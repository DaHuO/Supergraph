def generator(orig, complexity):
    new = orig
    for i in range(complexity-1):
        revised = ""
        for c in new:
            if c == 'L':
                revised += orig
            else:
                revised += 'G'*len(orig)
        new = revised
    return new

cases = int(raw_input().strip())
out = open('output.txt', 'w')

for case in range(cases):
    (orig_size, complexity, students) = [int(x) for x in raw_input().strip().split()]
    if orig_size != students:
        print "lies"
    res = [x+1 for x in range(0, orig_size**complexity, orig_size**(complexity-1))]

    s = "Case #"+str(case+1)+": "+' '.join([str(x) for x in res])+'\n'
    out.write(s)
    # print(s)
