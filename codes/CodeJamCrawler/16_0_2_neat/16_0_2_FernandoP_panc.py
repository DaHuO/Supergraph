
ninput = int(raw_input())
for j in range(ninput):
    vec = raw_input()
    l = len(vec)

    changif = '-'
    counter = 0
    for i in range(l):
        if vec[l-1-i] == changif:
            counter += 1
            if changif == '-':
                changif = '+'
            else:
                changif = '-'

    print "Case #"+str(j+1)+":",
    print counter




