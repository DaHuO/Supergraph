#!/usr/bin/env python


def changeLetter(letter):
    if(letter == '+'):
        letter = '-'
    else:
        letter = '+'
    return letter


def changeStack(stack):
    i = 1
    newStack = []
    newStack.append(changeLetter(stack[0]))
    while(i < len(stack) and stack[i] == stack[i-1]):
        newStack.append(changeLetter(stack[i]))
        i += 1
    while(i < len(stack)):
        newStack.append(stack[i])
        i+=1
    return newStack

N = int(raw_input())

i = 1

while i <= N:
    pancakes = raw_input()
    b = False
    count = 0
    while not b:
        b = True
        for x in pancakes:
            if x == '-':
                b = False
        if b == False:
            pancakes = changeStack(pancakes)
            count += 1
    print "Case #"+ str(i)+ ":",
    print count
    i+=1
