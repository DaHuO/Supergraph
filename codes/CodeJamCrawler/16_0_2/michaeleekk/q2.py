#!/usr/local/bin/python3

def count_change(s):
    count = 0
    c = s[0]
    for i in s[1:]:
        if c != i:
            count += 1
            c = i
    return count

def result(s):
    if '-' not in s:
        return 0
    elif '+' not in s:
        return 1
    elif s[0] == '-' and s[-1] == '-':
        return count_change(s)+1
    elif s[0] == '-' and s[-1] == '+':
        return count_change(s)
    elif s[0] == '+' and s[-1] == '-':
        return count_change(s)+1
    elif s[0] == '+' and s[-1] == '+':
        return count_change(s)

if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s = input()
        print("Case #{}: {}".format(i, result(s)))
