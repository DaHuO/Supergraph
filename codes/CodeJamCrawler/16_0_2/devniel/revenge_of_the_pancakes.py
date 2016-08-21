#Uses python3
import sys

"""
@author Daniel Flores
@date 9/04/2016
"""

def MinFlips(stack):
    #First mem = 0, to handle mem[i-1] first time
    mem = [0] * (len(stack)+1)
    stack = ['*'] + stack
    flips = 0
    for i in range(1, len(stack)):
        pancake = stack[i]

        #print("pancake : ", pancake)

        if pancake == "+":
            mem[i] = mem[i-1]
        else:
            last_pancake = stack[i-1]
            if last_pancake == pancake:
                mem[i] = mem[i-1]
            elif last_pancake == '*':
                mem[i] = 1
            else:
                mem[i] = mem[i-1] + 2

    return mem[len(stack)-1]


if __name__ == '__main__':

    #test()
    f = open('output', 'w')
    #f = None
    input = sys.stdin.read()
    data = list(input.split())
    T = int(data[0])
    for i in range(1,T+1):

        pancakes = list(data[i])

        if f:
            if i == T:
                f.write("Case #" + str(i) + ": " + str(MinFlips(pancakes)))
            else:
                print("Case #" + str(i) + ": " + str(MinFlips(pancakes)) , file=f)
        else:
            print("Case #" + str(i) + ": " + str(MinFlips(pancakes)))
