import fileinput

def diff_index(lst):
    assert lst != []

    prev = lst[0]
    for i in range(len(lst)):
        if lst[i] != prev:
            return i
    return -1

def opposite(x):
    return {'-': '+', '+': '-'}[x]

def solve(stack):
    count = 0
    while stack != []:
        i = diff_index(stack)
        if i == -1:
            return count if stack[0] == '+' else count + 1
        stack = stack[i-1:]
        stack[0] = opposite(stack[0])
        count += 1
    return count

def main():
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        stack = list(line.strip())
        print("Case #{}: {}".format(i, solve(stack)))

if __name__ == "__main__":
    main()
