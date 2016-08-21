def countingSheep(n):
    if n == 0:
        return 'INSOMNIA'
    arr = [False for i in range(10)]
    updateNum(n, arr)
    curN = n
    while not allSeen(arr):
        curN += n
        updateNum(curN, arr)
    return curN
          
def allSeen(a):
    index = 0
    while (index < 10):
        if a[index] == True:
            index += 1
        else:
            return False
    return True

def updateNum(n, arr):
    while n != 0:
        arr[n % 10] = True
        n = n // 10

def main():
    t = int(input())
    for i in range(1, t+1):
        case = int(input())
        print("Case #{}: {}".format(i, countingSheep(case)))

if __name__ == "__main__":
    main()