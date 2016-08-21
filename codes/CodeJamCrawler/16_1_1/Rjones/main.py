
def lastword(inputstr, caseno):
    tempstr = ""

    for x in range(len(inputstr)):
        if x == 0:
            tempstr = inputstr[x]
            continue

        if ord(inputstr[x]) >= ord(tempstr[0]):
            tempstr = inputstr[x] + tempstr

        else:
            tempstr = tempstr + inputstr[x]

    print("Case #%d: %s" % (caseno, tempstr))

def main():
    numberofcases = int(input())

    for x in range(numberofcases):
        lastword(input(), (x+1))

if __name__ == "__main__": main()