# -*- coding: utf-8 -*-


def solve(word):
    w = word[0]
    for c in word[1:]:
        if ord(c) >= ord(w[0]):
            w = c + w
        else:
            w = w + c
    return w


t = int(input())
for i in range(1,t+1):
    word = input()
    print("Case #" + str(i) + ": " + solve(word))
