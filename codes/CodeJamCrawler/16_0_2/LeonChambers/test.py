#!/usr/bin/env python3

class Stack:
    def __init__(self, pancakes):
        self.pancakes = pancakes

    def flip(self, i):
        top = self.pancakes[:i]
        top.reverse()
        top = [(i + 1) % 2 for i in top]
        return Stack(top + self.pancakes[i:])

    def reduce(self):
        pancakes = []
        curr = self.pancakes[0]
        for pancake in self.pancakes:
            if pancake != curr:
                pancakes.append(curr)
                curr = pancake
        pancakes.append(curr)
        return Stack(pancakes)

    def nexts(self):
        for i in range(len(self)):
            yield self.flip(i+1).reduce()

    def is_done(self):
        return self.pancakes == [1]

    def __str__(self):
        return str(self.pancakes)

    def __len__(self):
        return len(self.pancakes)

def output(i, ans):
    print("Case #{}: {}".format(i+1, ans))

T = int(input())
S = []
for i in range(T):
    S.append([char == '+' for char in input()])

for i in range(len(S)):
    s = S[i]
    stack = Stack(s).reduce()
    if stack.is_done():
        output(i, 0)
        continue
    num_flips = 0
    possibles = [stack]
    is_done = False
    best = len(stack)
    while True:
        num_flips += 1
        nexts = []
        for stack in possibles:
            for sub in stack.nexts():
                if sub.is_done():
                    is_done = True
                    break
                if len(sub) < best:
                    best = len(sub)
                if len(sub) < best+1:
                    nexts.append(sub)
        if is_done:
            output(i, num_flips)
            break
        possibles = nexts
