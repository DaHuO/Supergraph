import collections
in_file = "A-large.in"
with open(in_file, "r") as r:
    num_cases = r.readline()
    cases = r.readlines()

num2words = { 0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', \
            6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}
uniq_lists = [{'G': 8, 'Z': 0, 'W': 2, 'X': 6, 'U': 4}, {'H': 3, 'F': 5}, {'V': 7, 'O': 1, 'I': 9}]

answers = []
for case in cases:
    s = case.strip()
    answer = ""
    c = collections.Counter(s)
    for uniq in uniq_lists:
        for l in uniq:
            freq = c[l]
            num = uniq[l]
            if freq:
                answer += str(num) * freq
                sub = collections.Counter(num2words[num] * freq)
                c.subtract(sub)
    answer2 = "".join(sorted(answer))
    answers.append(answer2)

with open("out.txt", "w") as w:
    for idx, answer in enumerate(answers):
        w.write("Case #{}: {}\n".format(idx+1, answer))