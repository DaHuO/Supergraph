def countingSheep(num):
    numArr = []
    for i in range(10):
        numArr.append(0)
    allNums = 0
    iterNum = num

    if (num == 0):
        iterNum = "INSOMNIA"
    else:
        while allNums < 10:
            tempNum = str(iterNum)
            for i in range(len(tempNum)):
                if (numArr[int(tempNum[i])] == 0):
                    allNums += 1
                    numArr[int(tempNum[i])] = 1
            iterNum += num
        iterNum -= num

    return iterNum

def main():

    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        num = countingSheep(int(input()))
        print ("Case #{}: {}".format(i, num))

if __name__=='__main__':
    main()