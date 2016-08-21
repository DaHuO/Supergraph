
def countSheep(number):
    numDict = {}
    numberList = []
    numberList.append(number)
    multiplyVal = 2
    orig_number = number
    while len(numDict) != 10:
        for char in number:
            if numDict.has_key(char):
                continue
            else:
                numDict[char] = 1
        if len(numDict) == 10:
            break
        # Check for special case
        if multiplyVal == 50 or multiplyVal == 1000:
            if all(x == numberList[0] for x in numberList):
                return "INSOMNIA"
            else:
                if multiplyVal > 1000:
                    return "INSOMNIA"
        numberInt = int(orig_number) * int(multiplyVal)
        number = str(numberInt)
        multiplyVal += 1
        numberList.append(number)
    return number
    


def main():
    n_testcases = int(raw_input())
    counter = 1
    inputList = []
    while n_testcases > 0:
        inputList.append(raw_input())
        n_testcases -= 1
    for num in inputList:
        value = countSheep(num)
        print "Case #%s: "%counter + value
        counter += 1

if __name__=="__main__":
    main()
