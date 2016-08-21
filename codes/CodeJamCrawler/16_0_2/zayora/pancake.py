def read_stack(s):
    return [True if c == "+" else False for c in s]

def flip(stack, n):
    picked = stack[:n]
    flipped = []
    for p in picked:
        flipped.append(not p)
    return list(reversed(flipped)) + stack[n:]

def smile(stack):
    j = 0
    while True:
        for i, p in enumerate(stack):
            if p != stack[0]:
                stack = flip(stack, i)
                j += 1
                break
        else:
            if False in stack:
                return j+1
            else:
                return j

tests = int(input())

results=[]
for test in range(tests):
    stack = read_stack(input())
    results.append("Case #{}: {}".format(test+1, smile(stack)))

for result in results:
    print(result)
