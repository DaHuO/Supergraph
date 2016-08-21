def largestIndex(arr):
    index = 0
    for x in range(len(arr)):
        if arr[x] > arr[index]:
            index = x
    second = index + 1
    if second == len(arr):
        second = 0
    for x in range(len(arr)):
        if arr[x] > arr[second] and x != index:
            second = x
    return index,  second

def getChar(i):
    return chr(65 + i)

def main():

    cases = int(raw_input())
    for case in range(1,  cases+1):
        parties= int(raw_input())
        total = [int(s) for s in raw_input().split(" ")]
        left = sum(total)
        done = []
        while max(total) > 0:
            largest,  second = largestIndex(total)
            majority = float(left - 1) / 2.0
            if total[second] > majority :
                done.append((largest,  second))
                left -= 2
                total[largest] -= 1
                total[second] -= 1
            else:
                done.append((largest,  -1))
                total[largest] -= 1
                left -= 1
        soFar = ""
        for x in done:
            if x[1] != -1:
                soFar = soFar + getChar(x[0]) + getChar(x[1]) + " "
            else:
                soFar = soFar + getChar(x[0]) + " "
        soFar.rstrip()
        print("Case #%s: %s" % (case, soFar))

main()
