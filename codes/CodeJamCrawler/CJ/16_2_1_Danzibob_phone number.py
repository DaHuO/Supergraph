def read(file):
    with open(file,'r') as f:
        inp = [line[:-1] if '\n' in line else line for line in f]
    for line in inp:
        yield line
def add_line(file,line):
    with open(file,'a') as f:
        f.write(line+"\n")

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters  = []
for d in digits:
    for l in d:
        if l not in letters:
            letters.append(l)
f = read('input.txt')
num_lines = int(next(f))
case_num = 1

def find_digits(s):
    counts = dict(zip(alph,[0]*26))
    for l in s:
        counts[l] += 1
    n = dict(zip(range(0,10),[0]*10))
    if counts["Z"] > 0:
        n[0] = counts["Z"]
        counts["O"] -= counts["Z"]
        counts["R"] -= counts["Z"]
        counts["E"] -= counts["Z"]
        counts["Z"] = 0
    if counts["W"] > 0:
        n[2] = counts["W"]
        counts["T"] -= counts["W"]
        counts["O"] -= counts["W"]
        counts["W"] = 0
    if counts["G"] > 0:
        n[8] = counts["G"]
        counts["T"] -= counts["G"]
        counts["H"] -= counts["G"]
        counts["I"] -= counts["G"]
        counts["E"] -= counts["G"]
        counts["G"] = 0
    if counts["X"] > 0:
        n[6] = counts["X"]
        counts["I"] -= counts["X"]
        counts["S"] -= counts["X"]
        counts["X"] = 0
    if counts["H"] > 0:
        n[3] = counts["H"]
        counts["T"] -= counts["H"]
        counts["R"] -= counts["H"]
        counts["E"] -= counts["H"]
        counts["E"] -= counts["H"]
        counts["H"] = 0
    if counts["R"] > 0:
        n[4] = counts["R"]
        counts["F"] -= counts["R"]
        counts["O"] -= counts["R"]
        counts["U"] -= counts["R"]
        counts["R"] = 0
    if counts["O"] > 0:
        n[1] = counts["O"]
        counts["E"] -= counts["O"]
        counts["N"] -= counts["O"]
        counts["O"] = 0
    if counts["F"] > 0:
        n[5] = counts["F"]
        counts["I"] -= counts["F"]
        counts["V"] -= counts["F"]
        counts["E"] -= counts["F"]
        counts["F"] = 0
    if counts["V"] > 0:
        n[7] = counts["V"]
        counts["S"] -= counts["V"]
        counts["N"] -= counts["V"]
        counts["E"] -= counts["V"]
        counts["E"] -= counts["V"]
        counts["V"] = 0
    if counts["I"] > 0:
        n[9] = counts["I"]
        counts["N"] -= counts["I"]
        counts["N"] -= counts["I"]
        counts["E"] -= counts["I"]
        counts["I"] = 0
    pn = ""
    for d in n:
        pn += str(d)*n[d]
    return ''.join(sorted(pn))

for case in f:
    case_text = "Case #{}: ".format(case_num)
    add_line('output.txt',(case_text+find_digits(case)))
    case_num += 1
