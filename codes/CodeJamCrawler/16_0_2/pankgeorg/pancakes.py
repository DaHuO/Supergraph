#!/usr/bin/python3
def flip(stack, count):
    hsh ={"+": "-", "-": "+"}
    for i in range(count):
        stack[i] = hsh[stack[i]]


def pack(stack):
    new_stack = [stack[0]]
    old = stack[0]
    for i in stack[1:]:
        if old != i:
            new_stack.append(i)
        old = i
    return new_stack


def pancakes(stack):
    stack = pack(list(stack))
    i = 0
    l = len(stack)
    while not all("+" == x for x in stack):
        flip(stack, l - stack[::-1].index('-'))
        i += 1
    return i


def codejammer():
    Rounds = int(input())
    for r in range(1, Rounds + 1):
        print("Case #{}: {}".format(r, pancakes(input())))

if __name__ == '__main__':
    codejammer()

