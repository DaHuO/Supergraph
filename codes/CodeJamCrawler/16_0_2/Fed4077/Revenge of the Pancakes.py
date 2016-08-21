f = open("B-large.in", "r")
t = int(f.readline().strip())

for j in range(t):
    s = f.readline().strip()
    count = 0
    cond = True
    while cond:
        if s.rfind("-") != -1:
            add = ""
            for i in range(len(s[0:s.rfind("-")+1])):
                if s[i] == "+":
                    add += "-"
                else:
                    add += "+"
            #print s, count, len(add)
            s = add + s[s.rfind("-")+1:]
            count += 1
        else:
            cond = False
    print "Case #" + str(j+1) + ": " + str(count)
                

f.close()
