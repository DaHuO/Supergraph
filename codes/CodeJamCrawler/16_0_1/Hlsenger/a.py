#reading input
f = open('A-large.in','r')
out = open ('out','w')

#Read number of cases
num = int(f.readline())

memory = []
for i in range(0,num):
    first_n = int(f.readline().strip('\n'))
    n = first_n
    sleeping = False
    memory = []
    if (n == 0):
        output = "Case #" + str(i+1) + ": INSOMNIA"
        print output
        out.write(output + '\n')
        sleeping = True
    while(not sleeping):
        for ch in str(n):
            if ch  not in memory:
                memory.append(ch)
        if(len(memory) >= 10):
            output = "Case #" + str(i+1) + ": " + str(n)
            print output
            out.write(output + '\n')
            sleeping = True
        else:
            n += first_n



