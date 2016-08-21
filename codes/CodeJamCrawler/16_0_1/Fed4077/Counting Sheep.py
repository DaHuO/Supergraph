from sys import stdout

f = open("A-large.in", "r")
t = int(f.readline().strip())

for j in range(t):
    n = int(f.readline().strip())
    if n == 0:
        print "Case #" + str(j+1) + ": " + "INSOMNIA"
        continue
    cond = True
    count = 1
    seen = []
    while cond:
        #print 1, seen, count
        for i in range(0, 10):
            #print 2, seen, count
            if str(n*count).count(str(i))> 0 and i not in seen:
                seen.append(i)
            if len(seen) > 9:
                cond = False
                count -= 1
                break
        count += 1
    stdout.write("Case #" + str(j+1) + ": " + str(n*count)+ "\n")

f.close()
