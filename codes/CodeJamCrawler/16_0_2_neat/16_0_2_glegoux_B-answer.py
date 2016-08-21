#!/usr/bin/env python3

def pancake(stack):
    n = len(stack)
    f = '+'*n
    k = 0
    while stack != f:
        i = 0
        s = stack[0]
        while s == stack[0]:
            i += 1
            if i <= n-1:
                s = stack[i]
            else:
                break
        stack = return_pancake(stack, i)
        k += 1
    return k

def return_pancake(stack, i):
    s = list(stack)
    for j in range(i):
        if s[j] == '-':
            s[j] = '+'
        else:
            s[j] = '-'
    return "".join(s)

def print_answer(n, result):
    res = ""
    if type(result) in [list, tuple]:
        res = " ".join(map(str, result))
    elif type(result) == int:
        res = str(result)
    elif type(result) == str:
        res = result
    print("Case #{}: {}".format(n, res))

def main():
    T = int(input())
    for t in range(T):
        stack = input()
        print_answer(t + 1, pancake(stack))

if __name__ == "__main__":
    main()
