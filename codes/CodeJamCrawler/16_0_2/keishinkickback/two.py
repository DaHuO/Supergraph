import fileinput
import collections

def pancake(string):

    stack = string[0]
    count = 0
    for s in string[1::]:
        if stack != s:
            count +=1
            stack = s

    if string[-1] =='-':
        count +=1
    return count



if __name__ == "__main__":
    f = fileinput.input()
    T=int(f.readline())
    for line in range(1,T+1):
         N = [x for x in f.readline().split()][0]
         print("Case #{0}: {1}".format(line, pancake(N)))

