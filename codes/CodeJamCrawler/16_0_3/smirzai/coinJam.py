import math
import random
import fileinput



def checkNumber(n):
    base = 2
    result = []
    while base <= 10:
        nn = int(n, base)
        i = 2
        end = int(math.sqrt(nn)) + 1
        found = False
        cnt = 0
        while i < end:
            if nn % i == 0:
                result += [str(i)]
                found = True
                break
            i += 1
            cnt += 1
            if cnt > 1000:
                break
        if not found:
            return False, []
        base += 1
    return True, result

def generateNumber(n):
    st = "1"
    for i in range(n-2):
        st += random.choice(['0', '1'])

    return st + "1"

def solve(n, j):
    for i in range(j):
        while True:
            adad = generateNumber(n)
            ok, result = checkNumber(adad)
            if ok:
                print (str(adad) + " " + " ".join(result))
                break



inputFile = fileinput.input();
#inputFile = f = open('sample.txt', 'r')
t = int(inputFile.readline())
for i in range(t):
    print("Case #" + str(i + 1))
    st = inputFile.readline()
    l = st.split(" ")
    l = list(map(int, l))
    solve(l[0], l[1])

