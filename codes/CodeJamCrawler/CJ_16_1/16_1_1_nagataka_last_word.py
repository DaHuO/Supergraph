#!/usr/bin/python

dataset = open('A-small.in','r')
#dataset = open('A-large.in','r')

def solve(word):
    last = ""
    for char in word:
        if(last == ""):
            last += char
        elif(char >= last[0]):
            last = char+last
        else:
            last += char

    return last


line_num = 0
for word in dataset:
    word = str.strip(word)
    if(line_num==0):
        line_num+=1
    elif word == "\n":
        line_num+=1
    elif word == "":
        line_num+=1
    else:
        length = len(word)
        last = solve(word)
        print("Case #"+str(line_num)+": "+last)
        line_num += 1