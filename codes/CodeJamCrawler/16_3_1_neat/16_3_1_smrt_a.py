answers = []
letters = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solve(p):
    d = {}
    for i, number in enumerate(p, 1):
        d[letters[i]] = number
    output = ""
    while d:
        ans = ""
        for i in range(2):
            new_list = sorted(d, key=d.__getitem__, reverse=True)
            if len(new_list) == 2 and d[new_list[0]] == d[new_list[1]] and i == 1:
                ans += ""
            elif new_list:
                d[new_list[0]] -= 1
                ans += str(new_list[0])
                if d[new_list[0]] == 0:
                    d.pop(new_list[0])
        ans += " "
        output += ans
    return output.rstrip()

with open("A-large.in") as f:
    lines = f.readlines()[1:]
    cases = lines[1::2]
    for i, item in enumerate(cases, start=1):
        answers.append("Case #{}: {}".format(i, solve([int(i) for i in item.split()])))

with open("answers.txt", "w") as f:
    f.write("\n".join(answers))
