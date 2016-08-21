from sets import Set
import sys
import fileinput

i = 0

for line in fileinput.input():
    if i > 0:
        n = int(line)
        nold = n
        sys.stdout.write("Case #" + str(i) + ": ")

        if n == 0:
            print "INSOMNIA"
        
        else:
            finished = False
            s = Set([])

            while finished == False:
                for c in str(n):
                    s.add(c)

                if len(s) == 10:
                    print str(n)
                    finished = True
           
                n = n + nold

    i = i + 1
