
with open("A-large.in") as casefile:
    cases = [int(line.strip()) for line in casefile if line.strip()]

_, *cases = cases

for i, case in enumerate(cases):
    seen = set()
    N = 0

    while len(seen) < 10 and case != 0:
        N += case
        for digit in str(N):
            seen.add(digit)

    print("Case #{}: {}".format(i+1, N if N else 'INSOMNIA'))