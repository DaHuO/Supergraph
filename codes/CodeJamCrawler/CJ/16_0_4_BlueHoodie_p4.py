import itertools
file = open("C:\Users\Luca\Downloads\D-small-attempt0.in", "r")
file2 = open("ans.txt", "w")

times = int(file.readline())

def make_cases(num):
    substrings = []
    stuff = ["G", "L", "L", "G"]
    for subset in itertools.permutations(stuff, num):
        if subset not in substrings:
            substrings.append(subset)
    return substrings

def check(subs):
    solutions = []
    poss = subs[::3]
    print poss

    return min(solutions)

for time in range(times):
    data = file.readline().split()
    k_or_seq = int(data[0])
    complexity = int(data[1])
    students = int(data[2])

    """cases = make_cases(k_or_seq)
    cases.append(("G" * k_or_seq))
    cases.append(("L" * k_or_seq))
    sequences = []
    for case in cases:
        s = ""
        origin = ""
        for c in case:
            origin = origin + c
        sequences.append(case)
        for com in range(complexity - 1):
            s = ""
            for char in case:
                if char == "L":
                    s = s + origin
                else:
                    s = s + "G" * k_or_seq

            case = s

        if s not in sequences:
            sequences.append(s)"""

    if students >= k_or_seq:
        answer = ""
        for x in range(k_or_seq):
            answer = answer + str(x + 1) + " "

        s = "Case #" + str(time + 1) + ": " + answer + "\n"
        print s
        file2.write(s)

    """elif len(check(sequences)) > students:
        s = "Case #" + str(time + 1) + ": IMPOSSIBLE"
        file2.write(s)
    else:
        answer = check(sequences)
        s = "Case #" + str(time + 1) + ": " + answer
        file2.write(s)"""