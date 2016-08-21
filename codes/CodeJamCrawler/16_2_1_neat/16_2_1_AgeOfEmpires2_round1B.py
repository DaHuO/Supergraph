import sys
import time

start_time = time.time()

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stdout = sys.__stdout__

def checker(s, e):
    d = dict(e)
    for i in s:
        try:
            if d[i] > 0:
                d[i] -= 1
            else:
                return False
        except KeyError:
            return False
    return True

def reduce(s, d):
    for i in s:
        d[i] -= 1
    return d

def convert(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

for testcases in range(int(input())):
    words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    name = input()
    keys = convert(name)
    ans = []
    try:
        if keys['U'] > 0:
            i = 4
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i],keys)
    except KeyError:
        pass
    try:
        if keys['Z'] > 0:
            i = 0
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    try:
        if keys['X'] > 0:
            i = 6
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    try:
        if keys['W'] > 0:
            i = 2
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    try:
        if keys['V'] > 0 and keys['F'] > 0:
            i = 5
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    try:
        if keys['V'] > 0:
            i = 7
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    try:
        if keys['O'] > 0:
            i = 1
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    try:
        if keys['N'] > 0:
            i = 9
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    try:
        if keys['I'] > 0:
            i = 8
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    try:
        if keys['E'] > 0:
            i = 3
            while checker(words[i], keys):
                ans += str(i)
                keys = reduce(words[i], keys)
    except KeyError:
        pass
    ans.sort()
    ans = ''.join(ans)
    sys.stdout = open("output.txt", "a")
    print("Case #" + str(testcases + 1) + ": " + ans)
    sys.stdout = sys.__stdout__
    print("Case #" + str(testcases + 1) + ": Done")

sys.stdout = sys.__stdout__
print(time.time() - start_time)