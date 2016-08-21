import random
nots = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")

def isIn(str1, str2):
    i = False
    str2 = list(str2)
    
    c = 0
    for char in str1:
        if char in str2:
            str2.pop(str2.index(char))
            c+=1

    if(c == len(str1)):
        i = True

    return (i, "".join(str2))




tests = int(input(""))
i = 0

while i < tests:
    raw = input("")

    ori = raw
    final = []
    loop = 0

    while raw:
        loop+=1
        j = random.randint(0,9)
        #print("trying ", j)

        t = isIn(nots[j], raw)
        if(t[0]):
            #print("Found ", j)
            final.append(j)
            raw = t[1]
        #print(raw)

        if(loop >= 10):
            final = []
            raw = ori
            loop = 0

    print("CASE #{}:".format(i+1),"".join([str(x) for x in sorted(final)]))

    i+=1
