# Language       : Python 3
# Compiled Using : py_compile
# Version        : Python 3.4.3


def add(a,b):
    if a == b:
        return 0
    if min(a,b) == 1 and max(a,b) == 2:
        return 2
    if min(a,b) == 1 and max(a,b) == 3:
        return 1
    if min(a,b) == 2 and max(a,b) == 3:
        return 3

    print("Error!")
    return 0


# ToDo Dynamic with map of seen things
def isTie(seq):
    if len(seq) <= 1:
        return False
    new_seq = []
    for i in range(0,len(seq), 2):
        result = add(seq[i], seq[i+1])
        if result == 0:
            return True
        else:
            new_seq.append(add(seq[i], seq[i+1]))
    return isTie(new_seq)


def transform(seq, P, R, S):
    newseq = ""
    for s in seq:
        if s == 1:
            newseq += "P"
            P -= 1
        if s == 2:
            newseq += "R"
            R -= 1
        if s == 3:
            newseq += "S"
            S -= 1
    return newseq, P, R, S


def constructTree(root, depth, P, R, S):
    if depth == 0:
        return [root]
    if root == 1:
        return constructTree(1, depth - 1, P, R, S) + constructTree(2, depth - 1, P, R, S)
    if root == 2:
        return constructTree(2, depth - 1, P, R, S) + constructTree(3, depth - 1, P, R, S)
    if root == 3:
        return constructTree(1, depth - 1, P, R, S) + constructTree(3, depth - 1, P, R, S)


def reorder_seq(seq, distance):
    for i in range(2*distance, len(seq)+1, 2*distance):
        # We can make a cut here and swap, should we?
        partA = seq[i-2*distance:i-distance]
        partB = seq[i-distance:i]
        if partB < partA:
            new_seq = seq[:i-2*distance] + partB + partA + seq[i:]
        if partB >= partA:
            new_seq = seq[:i-2*distance] + partA + partB + seq[i:]
        seq = new_seq
    return seq


def optimal(seq, length):
    # Reorder the list to be optimal:
    while True:
        old_seq = seq
        #print(old_seq)
        for i in range(1, length+1):
            distance = 2**i

            seq = reorder_seq(seq, distance)
            #print(distance, seq)
        if seq == old_seq:
            return seq

    return seq

with open("A-large.in") as f:
    data = f.readlines()


test_case_counter = 0
test_cases = int(data[0][:-1])
line_counter = 1
for _ in range(test_cases):
    test_case_counter += 1
    numbers = data[line_counter][:-1].split(" ")
    line_counter += 1
    N, R, P, S = int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])

    # 3 Options, the winner is P, R, or S:
    sequence1, P1, R1, S1 = transform(constructTree(1, N, P, R, S), P, R, S)  # P
    sequence2, P2, R2, S2 = transform(constructTree(2, N, P, R, S), P, R, S)  # R
    sequence3, P3, R3, S3 = transform(constructTree(3, N, P, R, S), P, R, S)  # S

    NTotal = 2 ** N
    P1, R1, S1
    if (P1 < 0 or R1 < 0 or S1 < 0) and (P2 < 0 or R2 < 0 or S2 < 0) and (P3 < 0 or R3 < 0 or S3 < 0):
        print("Case #" + str(test_case_counter) + ": " + "IMPOSSIBLE")
        continue

    list = []
    counter = 0
    if not (P1 < 0 or R1 < 0 or S1 < 0):
        list.append(optimal(sequence1, N))
        counter += 1
    if not (P2 < 0 or R2 < 0 or S2 < 0):
        list.append(optimal(sequence2, N))
        counter += 1
    if not (P3 < 0 or R3 < 0 or S3 < 0):
        list.append(optimal(sequence3, N))
        counter += 1
    if counter > 1:
        sortedList = sorted(list)
    else:
        sortedList = list

    print("Case #" + str(test_case_counter) + ": " + str(sortedList[0]))
