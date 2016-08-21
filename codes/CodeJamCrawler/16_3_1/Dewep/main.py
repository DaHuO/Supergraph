#!/usr/bin/env python3

T = int(input())

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_majority_absolute(state, total, first, second):
    state[0]["n"] -= first
    state[1]["n"] -= second
    total -= first + second
    res = True
    for elem in state:
        if elem["n"] < 0 or total > 0 and elem["n"] * 100 / total > 50:
            res = False
            break
    state[0]["n"] += first
    state[1]["n"] += second
    return res

def find_evacuation(state, total):
    path = ""
    state = sorted(state, key=lambda elem: elem["n"], reverse=True)
    while state[0]["n"] > 0:
        if is_majority_absolute(state, total, 2, 0):
            path += " " + state[0]["l"]*2
            state[0]["n"] -= 2
            total -= 2
        elif is_majority_absolute(state, total, 1, 1):
            path += " " + state[0]["l"] + state[1]["l"]
            state[0]["n"] -= 1
            state[1]["n"] -= 1
            total -= 2
        else:
            path += " " + state[0]["l"]
            state[0]["n"] -= 1
            total -= 1
        state = sorted(state, key=lambda elem: elem["n"], reverse=True)
    return path

for t in range(0, T):
    state = []
    number = int(input())
    numbers = [int(n) for n in input().split(" ")]
    total = 0
    for i in range(number):
        state.append({"l": letters[i], "n": numbers[i]})
        total += numbers[i]
    print("Case #%d:%s" % (t + 1, find_evacuation(state, total)))
