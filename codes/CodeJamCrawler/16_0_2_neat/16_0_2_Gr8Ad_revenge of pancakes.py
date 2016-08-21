tests = int(input())
def done(l):
    for e in range(0, len(l)):
        if l[e] != "+":
            return False
    return True

def maxminus(l):
    for k in range(0, len(l)):
        if l[k] != "-":
            if k == 0:
                return -2
            return k
##    return -2

for i in range(0, tests):
    cur = input()
    pancakes = list(cur)
    moves = 0
    while not done(pancakes):
##        print("in pmain")
        if pancakes.index("-") != 0 and pancakes[0:pancakes.index("-")] == list("+"*pancakes.index("-")):
            for y in range(0, pancakes.index("-")):
                pancakes[y] = "+"
            curpan = "-"
            q = pancakes.index("-")
            try:
                while pancakes[q] == "-":
##                    print("p",pancakes)
##                    print("q",q)
##                    print("curp",curpan)
                    pancakes[q] = "+"
                    q += 1
##                    print("in curpan")
            except IndexError:
                pass
            moves += 2
            
            
        else:
            for j in range(len(pancakes)-1, -1, -1):
##                print(1)
##                print(j)
                if pancakes[j] == "-":
                    for p in range(0, j+1):
                        if pancakes[p] == "+":
                            pancakes[p] = "-"
                        else:
                            pancakes[p] = "+"
##                        print("P",pancakes)
                    pancakes[0:j+1] = reversed(pancakes[0:j+1])
##                    print(pancakes)
                    moves += 1
                    break
    print("Case #" + str(i+1) + ": " + str(moves))
##        for j in range(0, len(pancakes)):
##            if j == maxminus(pancakes)-1 or maxminus(pancakes) == -2:
##                if pancakes[j] == "-":
##                    for p in range(0, j+1):
##                        print(p)
##                        if pancakes[p] == "+":
##                            pancakes[p] = "-"
##                            print("changed")
##                        else:
##                            pancakes[p] = "+"
##                            print("changed2")
##                    print("P",pancakes)
##                    pancakes[0:j+1] = reversed(pancakes[0:j+1])
##                    print("r",pancakes)
