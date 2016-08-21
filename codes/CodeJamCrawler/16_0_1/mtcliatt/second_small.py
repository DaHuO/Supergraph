def solve(num):
    if num == 0:
        return "INSOMNIA"

    digits = [0] * 10
    start = num

    while True:
        s = str(num)
        for c in s:
            digits[int(c)] = 1

        if( good(digits) ):
            return num
        else:
            num += start


def good(arr):
    for i in arr:
        if i == 0:
            return False
    return True

cases = int(input())
for i in range(cases):
    case = int(input())
    print("Case #{}: {}".format(i+1, solve(case)))
