def solution():
    pancakes = input()

    lastchar = pancakes[0]
    result = 1

    for c in pancakes[1:]:
        if c != lastchar:
            lastchar = c
            result += 1

    if lastchar == '+':
        result -= 1

    return result

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{}: {}".format(i, solution()))
