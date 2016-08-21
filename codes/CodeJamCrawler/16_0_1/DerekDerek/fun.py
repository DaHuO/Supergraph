cases = raw_input()
for x in range(1, int(cases)+1):
    arr = [0,1,2,3,4,5,6,7,8,9]
    narr = []
    og = raw_input()
    if og == "0":
        print "Case #"+ str(x) + ": INSOMNIA"
        continue
    n = og
    count = 2
    done = False
    while not done:
        ns = str(n)
        for l in ns:
            if int(l) not in narr:
                narr.append(int(l))
                narr.sort()
                if narr == arr:
                    done = True
        if not done:
            n = int(og)*count
            count = count + 1
        else:
            print "Case #"+ str(x) + ": " + str(n)
