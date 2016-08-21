def flip(boollist):
    return [not i for i in boollist]

def checkAllTrue(boollist):
    if boollist.count(True) == len(boollist):
        return True
    return False

def recursiveFlip(boollist, n=0):
    if checkAllTrue(boollist):
        return n
    elif(boollist[-1] == False):
        return recursiveFlip(flip(boollist[0:-1]), n+1)
    else:
        return recursiveFlip(boollist[0:-1], n)

def plusminus(x):
    if(x == "+"):
        return True
    else:
        return False

def inputToList(inlist):
    inlist = list(inlist)
    inlist = map(plusminus, inlist)
    return list(inlist)

T = int(input())
results = [None]*T
for j in range(T):
    results[j] = recursiveFlip(inputToList(input()))
for i in range(T):
    print("Case #{}: {}".format(i+1, results[i]))