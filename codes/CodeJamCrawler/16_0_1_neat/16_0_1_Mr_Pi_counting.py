import sys

if __name__ == "__main__":
    f = open(sys.argv[1])
    s = int(f.readline().strip())
    for j in xrange(s):
        i = int(f.readline().strip())
        if i == 0:
            print("Case #"+str(j+1)+": INSOMNIA")
            continue
        x = i
        digit = set(str(x))
        while len(digit) < 10:
            x += i
            digit.update(set(str(x)))
        #print(str(i)+" "+str(x))
        print("Case #"+str(j+1)+": "+str(x))
    f.close()
