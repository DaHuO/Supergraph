import sys
import time

def count(start):
    start = int(start)
    #print("start= " + str(start))
    if start == 0:
        print("INSOMNIA")
        return

    array=[]
    i = 1
    n = start
    while True:
        #print("n= " + str(n*i))
        for char in str(n*i):
            if not char in array:
                array.append(char)
        if len(array) == 10:
            print(n*i)
            return
        i += 1
        #time.sleep(1)



if __name__ == "__main__":
    T = int(raw_input())
    for i in xrange(1, T + 1):
        N = raw_input()
        sys.stdout.write("Case #{0}: ".format(i))
        count(N)
