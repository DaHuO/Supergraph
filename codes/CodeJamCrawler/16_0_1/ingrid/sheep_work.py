input_file = '../A-small-attempt0.in'
f = open(input_file, 'r')
#pay day loans in Oregon
output = open('../sheep_output.txt', 'w')
for i, t in enumerate(f):
    x = False
    if i > 0:
        print t.rstrip('\n')
        cache = []
        n = 1
        while len(set(cache)) != 10:
            cache += sorted(str(int(t)*n))
            n+=1
            if n > 10 and len(set(cache)) < 2:
                x = True
                break
        if x == True:
            y = "Case #"+str(i)+": INSOMNIA"
            output.write(y+"\n")
            print y
        else:
            y = "Case #"+str(i)+": "+str((n-1)*int(t))
            output.write(y+"\n")
            print y
