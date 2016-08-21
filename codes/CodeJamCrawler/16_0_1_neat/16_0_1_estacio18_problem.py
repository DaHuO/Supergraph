# Just a python problem

n = int(raw_input())

for i in range(n):

    s = set([])
    k = int(raw_input())

    if not k:
        print ("Case #%d: INSOMNIA" % (i+1))

    else:
        counter = 1
        while True:

            m = k * counter
            for j in set(list(str(m))):
                s.add(j)
                if(len(s) == 10):
                    break
            if(len(s) == 10):
                print ("Case #%d: %d" % ((i+1), m))
                break

            counter += 1
