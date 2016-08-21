from collections import Counter
from string import ascii_uppercase

file = "A-large.in"

def can_leave(counter, leavers):
    copy = Counter(counter);
    copy.subtract(leavers)
    number_of_stayers = sum(copy.values())

    for value in copy.values():
        if value < 0:
            return False

    for letter, count in copy.most_common(3):
        if 2 * count > number_of_stayers:
            return False

    return True


def senate_evacuation(P):
    counter = Counter()
    for index, count in enumerate(P):
        counter[ascii_uppercase[index]] = count

    plan = []

    while sum(counter.values()):
        most_common = [letter for letter, count in counter.most_common(2) if count]
        next_evacuate = None

        two_of_first = 2 * most_common[0]
        one_of_each = ''.join(most_common)
        one_of_first = most_common[0]

        if can_leave(counter, two_of_first):
            next_evacuate = two_of_first
        elif can_leave(counter, one_of_each):
            next_evacuate = one_of_each
        else:
            next_evacuate = one_of_first

        plan.append(next_evacuate)
        counter.subtract(next_evacuate)

    return plan


with open(file) as handle:
  T = int(handle.readline())

  for t in range(T):
    N = int(handle.readline())
    P = map(int, handle.readline().strip().split())

    print "Case #{}: {}".format(t + 1, ' '.join(senate_evacuation(P)))
