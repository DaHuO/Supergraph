import sys

#add digits of n to the list
def adddigits(n, list):
    #print list
    nstr = str(n)
    for c in nstr:
        if c not in list:
            list.append(c)
            #print("added " + c)

def lastnum(n):
    #print("checking last num of " + str(n))
    if n == 0:
        return "INSOMNIA"

    curnums = []

    #add initial n
    i = 1
    adddigits(n * i, curnums)

    while len(curnums) != 10:
        i = i + 1
        adddigits(n * i, curnums)    

    return (n * i)

def main():
    #print("reading " + sys.argv[1])
    f = open(sys.argv[1])

    t = int(f.readline())

    for i in range(1, t+1):
        n = int(f.readline())
        last = lastnum(n)
        print("Case #" + str(i) + ": " + str(last))

main()
