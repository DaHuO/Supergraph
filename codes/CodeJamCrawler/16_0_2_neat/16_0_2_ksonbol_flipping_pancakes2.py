file_name = "B-large.in"

with open(file_name, "r") as r:
    num_cases = r.readline()
    cases = r.readlines()

def flip(s):
    reverse = s[::-1]
    trans_table = str.maketrans({"+": "-", "-": "+"})
    return reverse.translate(trans_table)

def opposite_side(side):
    return "-" if side == "+" else "+"

def count_flips(s):
    count = 0
    while s.count("-") != 0:
        top = s[0]
        first_opposite = s.find(opposite_side(top))
        if first_opposite == -1:
            s = flip(s)
        else:
            s = flip(s[:first_opposite]) + s[first_opposite:]
        count += 1
    return count

answers = []
for case in cases:
    s = case.strip()
    answers.append(count_flips(s))

with open("out.txt", "w") as w:
    for idx, answer in enumerate(answers):
        w.write("Case #{}: {}\n".format(idx+1, answer))