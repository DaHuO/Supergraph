t = int(input())

def solve(string):
    s = ""
    for letter in string:
        if s == "" or letter >= s[0]:
            s = letter + s
        else:
            s = s + letter
    return s


for i in range(1, t + 1):
    s = input()
    solution = solve(s)
    print("Case #{}: {}".format(i, solution))
