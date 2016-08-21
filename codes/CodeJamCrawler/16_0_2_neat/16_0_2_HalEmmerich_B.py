#!/bin/python3


def flip(stack, i):
    for l in range(i, -1, -1):
        if stack[l] == '+':
            stack[l] = '-'
        else:
            stack[l] = '+'

def main():
    runs = int(input())



    for i in range(runs):
        flips = 0
        stack = list(input())
        for x in range(len(stack)):
        #for cake in stack:
            if((x+1) < len(stack)):

                if( stack[x] != stack[x+1]):
                    flip(stack, x)
                    flips += 1

        if(stack[0] == '-'):
            flips += 1

        print("Case #" + str(i+1) + ": " + str(flips))
main()
