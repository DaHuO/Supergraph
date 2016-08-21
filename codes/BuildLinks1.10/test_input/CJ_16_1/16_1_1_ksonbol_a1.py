in_file = "A-large.in"
with open(in_file, "r") as r:
    num_cases = r.readline()
    cases = r.readlines()

answers = []
for case in cases:
    s = case.strip()
    word = s[0]
    for char in s[1:]:
        if char >= word[0]:
            word = char + word
        else:
            word = word + char
    answers.append(word)

with open("out.txt", "w") as w:
    for idx, answer in enumerate(answers):
        w.write("Case #{}: {}\n".format(idx+1, answer))