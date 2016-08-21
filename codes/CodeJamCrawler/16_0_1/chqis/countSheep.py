import sys

def scanN(N, numsSeen):
    for i in range(len(str(N))):
        numsSeen[int(str(N)[i])] = True
    return numsSeen

def check(numsSeen):
    for i in numsSeen:
        if not i: return False
    return True

def main():
    T = int(sys.stdin.readline())
    j = 0
    for i in range(T):
        j+=1
        numsSeen = [False]*10
        N = int(sys.stdin.readline())
        if N == 0:
            print("Case #"+str(j)+": INSOMNIA")
            continue

        No = N
        while(True):
            numsSeen = scanN(N, numsSeen)
            if check(numsSeen):
                print("Case #"+str(j)+": "+str(N))
                break
            N += No
main()
