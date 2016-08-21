digitArray = [0,0,0,0,0,0,0,0,0,0]
def digitCounter(n):
    while n != 0:
        digitArray[int(n%10)] += 1
        n = int(n/10)

def clearArray():
    for i in range(0,10):
        digitArray[i] = 0

def checkArray():
    for i in range(0,10):
        if digitArray[i] == 0:
            return False
    return True

m = int(input())
for l in range(1,m+1):
    n = int(input())
    if n == 0:
        print("Case #",l,": INSOMNIA", sep='')
    else:
        clearArray()
        i = 0
        while checkArray() == False:
            i += 1
            digitCounter(n*i)
        print("Case #",l,": ",n*i, sep='')
