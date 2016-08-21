from tqdm import tqdm
answers = ["INSOMNIA"]
def get_answer(n):
    digits = set()
    i = 1
    while len(digits) < 10:
        txt = str(i*n)
        for j in txt:
            digits.add(j)
        i += 1
    answers.append(str((i-1)*n))

for i in tqdm(range(1, 10**6 + 1)):
    get_answer(i)

n = int(raw_input())
for i in range(1, n+1):
    k = int(raw_input())
    print "Case #{}: {}".format(i, answers[k])
