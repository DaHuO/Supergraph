T = int(input())

def findLargest(num):
    origNum = num
    numsSeen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while numsSeen != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
        for number in decompose(num):
            numsSeen[number-1] = 1
        num += origNum
    return (num - origNum)

def decompose(num):
    return list(map(int, list(str(num))))

for caseNum in range(1, T+1):
    N = int(input())
    if N == 0:
        print("Case #%d: INSOMNIA" %(caseNum))
    else:
        ans = findLargest(N)
        print("Case #%d: %d" %(caseNum, ans))
    
