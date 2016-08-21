import sys

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    N = int(sys.stdin.readline().strip())
    orders = []
    for c in range (2 * N - 1):
        orders.append([int(x) for x in sys.stdin.readline().strip().split(' ')])
    index = 0
    sequences = []
    missing = -1
    while index < N:
        min_height = 99999
        for order in orders:
            if order[index] < min_height:
                min_height = order[index]
        sequence = []
        for order in orders:
            if order[index] == min_height:
                sequence.append(order)
        for used in sequence:
            orders.remove(used)
        if len(sequence) == 1:
            missing = index
        index += 1
        sequences.append(sequence)
    missing_order = []
    ref = sequences[missing][0]
    for c in range(N):
        if c != missing:
            if sequences[c][0][missing] == ref[c]:
                missing_order.append(sequences[c][1][missing])
            else:
                missing_order.append(sequences[c][0][missing])
        else:
            missing_order.append(sequences[c][0][missing])
    print("Case #{}: {}".format(i, " ".join([str(x) for x in missing_order])))
