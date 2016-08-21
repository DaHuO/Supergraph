import sys


def fractile_answer(k, c, s):
    """
    Trivially naive, but should work under S=K conditions of small set
    """
    return range(1, s+1)

sys.stdin.readline()  # disregard first line. no need to use this count
count = 0
for current_line in sys.stdin:
    count += 1
    k, c, s = [int(i) for i in current_line.split()]
    answer = fractile_answer(k, c, s)
    print("Case #{0}: {1}".format(count, ' '.join([str(i) for i in answer])))
