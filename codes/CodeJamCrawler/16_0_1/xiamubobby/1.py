ATTEMPT = 0

T = 0

#fi = open("A-small-attempt{}.in".format(ATTEMPT), encoding="UTF-8")
fi = open("A-large.in", encoding="UTF-8")
ls = fi.readlines()
T = int(ls[0])
base_numbers = ls[1:]
base_numbers = [int(bn.strip()) for bn in base_numbers]
results = []
for base_number in base_numbers:
    if base_number == 0:
        results.append(-1)
    else:
        digits = set()
        n = base_number
        while len(digits) != 10:
            for digit in [int(chara) for chara in str(n)]:
                digits.add(digit)
            n += base_number
        results.append(n - base_number)

#fo = open("A-small-attempt{}.out".format(ATTEMPT), 'w', encoding="UTF-8")
fo = open("A-large.out", 'w', encoding="UTF-8")
i = 1
for result in results:
    fo.write("Case #{}: ".format(i))
    fo.write(str(result) if result != -1 else "INSOMNIA")
    fo.write('\n')
    i += 1
