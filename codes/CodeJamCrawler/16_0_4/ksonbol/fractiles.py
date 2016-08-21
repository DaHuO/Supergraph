file_name = "D-small-attempt0.in"

with open(file_name, "r") as r:
    num_cases = int(r.readline().strip())
    cases = r.readlines()
answers = []
for case in cases:
    line = case.strip().split()
    k,c, s = [int(x) for x in line]
    if k == s:
        # there is always a solution
        step = range(1, (k**c) + 1, k ** (c-1))
        positions = list(str(x) for x in step)
        answer = " ".join(positions)
        answers.append(answer)

with open("out.txt", "w") as w:
    for idx, answer in enumerate(answers):
        w.write("Case #{}: {}\n".format(idx+1, answer))