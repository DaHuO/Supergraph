input_file = '../B-small-attempt0.in'
f = open(input_file, 'r')

output = open('../pancake_output.txt', 'w')
for i, t in enumerate(f):
    if i > 0:
#         print list(t.rstrip("\n"))
        changes = 0
        for j,pancake in enumerate(t[0:-2]):
            if pancake != t[j+1]:
                changes += 1
        if t[-2] == '-':
            flips = changes + 1
        else:
            flips = changes
        y = "Case #"+str(i)+": "+str(flips)
        output.write(y+"\n")
        print y
        
