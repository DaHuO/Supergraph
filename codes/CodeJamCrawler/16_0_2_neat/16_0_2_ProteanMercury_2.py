f = open('B-large.in', 'r')
o = open('output', 'w')
T = f.readline()
F = f.readlines()
for i in range(int(T)):
    print "Case", i+1
    o.write("Case #")
    o.write(str(i+1))
    o.write(": ")
    stack = F[i].strip()
    flipcount = 0
    print stack
    for j in range(len(stack)):
        if j<len(stack)-1:
            if stack[j] != stack[j+1]:
                flipcount = flipcount + 1
        else:
            if stack[j] == '-':
                flipcount = flipcount + 1
    print flipcount
    o.write(str(flipcount))
    o.write("\n")
o.close()
