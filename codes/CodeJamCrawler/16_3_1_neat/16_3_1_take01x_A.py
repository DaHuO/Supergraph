import sys

file = open("A-large.in")

T = int(file.readline())
index = 1
for i in xrange(T):
    N = int(file.readline())
    list = file.readline().rstrip("\n").split(" ")
    list = map(lambda x:int(x), list)
    print("Case #%d: " % index),
    index = index + 1
    while True:
        for k in xrange(2):
            if k == 1 and list.count(1) == 2 and max(list) == 1:
                break
            else:
                tmp =  list.index(max(list))
                list[tmp] = list[tmp] - 1
                sys.stdout.write("%s" % chr(ord('A') + tmp))
        print(" "),
        if max(list) == 0:
            break
    print("")
