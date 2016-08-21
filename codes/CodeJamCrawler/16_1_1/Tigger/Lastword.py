import sys

def doStuff(line):
    newS = ""
    newS = line[0]
    line = line[1:]
   
    for c in line:
        if newS[0] <= c:
            newS = c + newS
        else:
            newS += c
    return newS


def main():
    f = sys.stdin
    f.readline()
    i = 0
    for line in f.readlines():
        i += 1
        doStuff(line.strip())
        print "Case #" + str(i) +  ": " +  doStuff(line).strip()


main()
