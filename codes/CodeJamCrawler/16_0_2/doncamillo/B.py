from numpy import array


with open("B-large.in") as casefile:
    cases = [line.strip() for line in casefile if line.strip()]
    _, *cases = cases

for i, case in enumerate(cases):
    flips = 0 if case[-1] == '+' else 1
    for a, b in zip(case[:-1], case[1:]):
        if a != b:
            flips += 1

    print("Case #{}: {}".format(i+1, flips))