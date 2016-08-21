def check(s):
    for c in s:
        if c == '-':
            return False
    return True

def flip(s):
    if len(s)==1:
        s[0] = '+'
        return s
    index = 0
    if s[0] == '-':
        while s[index]=='-':
            index+=1
            if index == len(s):
                break
    else:
        while s[index]=='+':
            index+=1
            if index == len(s):
                break
    
    
    for i in range(index):
        if s[i] == '-':
            s[i] = '+'
        else:
            s[i] = '-'
    
    return s
            

infile = open("B-large.in", "r")
outfile = open("B-large.out", "w")

t = infile.readline()
print(t)
casenumber = 1
for line in infile:
    count = 0
    s = list(line[:-1])
    
    while not check(s):
        s = flip(s)
        count+=1
    print("Case #{}: {}".format(casenumber, count), file=outfile) 
    casenumber+=1
print("done")
infile.close()
outfile.close()
