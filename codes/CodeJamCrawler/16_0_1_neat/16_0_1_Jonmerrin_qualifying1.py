import os


def allTrue(l):
    for i in l:
        if i == False:
            return False
    return True

def solveSheep(path):
    with open(path, "rt") as fin:
        stuff = fin.read().splitlines()
    string = ""
    numbers = [False]*10    
    for i in xrange(1, len(stuff)):
        if (int(stuff[i]) == 0):
            string = string + "Case #%d: INSOMNIA\n" %(i)
        else:
            count = 1
            a = int(stuff[i])
            while not(allTrue(numbers)):
                n = a * count
                while n != 0:
                    numbers[n%10] = True
                    n = n/10
                count = count + 1
            string = string + "Case #%d: %d\n" %(i, a*(count-1))
            numbers = [False] * 10

    with open("solution1 large.txt", "wt") as fout:
        fout.write(string)
