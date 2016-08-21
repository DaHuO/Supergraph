file_name = "A-large.in"
with open(file_name, "r") as r:
    num_cases = r.readline()
    cases = r.readlines()
answers = []
for case in cases:
    n = int(case.strip())
    if n == 0:
        answers.append("INSOMNIA")
        continue
    seen_digits = set(int(x) for x in list(str(n)))
    i = 2
    while seen_digits != set(range(0, 10)):
        largest_num = i * n
        new_digits = set(int(x) for x in list(str(largest_num)))
        seen_digits.update(new_digits)
        i += 1
    answers.append(largest_num)

with open("out.txt", "w") as w:
    for idx, answer in enumerate(answers):
        w.write("Case #{}: {}\n".format(idx+1, answer))