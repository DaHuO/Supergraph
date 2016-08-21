import itertools

def flip(arr, i):
    arr = list(arr)
    start = 0

    if i == 0:
        i = first_last_plus_sign(arr)

    while start < i:
        if arr[start] == "-":
            arr[start] = "+"
        elif arr[start] == "+":
            arr[start] = "-"
        start += 1

    arr[0:i] = reversed(arr[0:i])

    return "".join(x for x in arr)


def first_last_plus_sign(arr):

    i = 0
    for c in arr:
        if c == "-":
            return i
        else:
            i += 1

def first_plus_sign(pancakes):

    s = 0
    while s < len(pancakes):
        if pancakes[s] == "-":
            s += 1
        else:
            return s

    return -1

def run_code():
    t = int(input())

    res = []
    for i in range(t):
        steps = 0
        pancakes = input()
        n = len(pancakes)
        target = "+" * n
        first_plus = first_plus_sign(pancakes)
        minus_target = "-" * n

        if first_plus == -1 and pancakes == minus_target:
            res.append([i+1, 1])
        elif pancakes == target:
            res.append([i+1, 0])
        else: #this starts with -
            while(pancakes != target):
                steps += 1
                pancakes = flip(pancakes, first_plus)
                first_plus = first_plus_sign(pancakes)

                if first_plus == -1:
                    res.append([i+1, steps + 1])
                    break

                if pancakes == target:
                    res.append([i+1, steps])
                    break

    for op in res:
        print("Case #" + str(op[0]) + ": " + str(op[1]))

if __name__ == "__main__":
    run_code()
