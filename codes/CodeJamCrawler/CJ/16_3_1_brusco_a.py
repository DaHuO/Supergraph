import heapq
import string


class Party(object):
    def __init__(self, name, remaining):
        super(Party, self).__init__()
        self.name = name
        self.remaining = remaining

    def evacuate(self):
        self.remaining -= 1

    def __cmp__(self, other):
        return other.remaining - self.remaining

    def __repr__(self):
        return "{}: {}".format(self.name, self.remaining)


case_count = int(raw_input())
for case_number in xrange(1, case_count + 1):
    raw_input()
    letters = list(string.ascii_uppercase)
    parties = []
    for letter_number, remaining in enumerate(raw_input().split()):
        heapq.heappush(parties, Party(letters[letter_number], int(remaining)))

    plan = []
    while True:
        if not parties:
            break

        first = heapq.heappop(parties)
        current_step = first.name

        second = parties[0]
        if second.remaining == first.remaining \
                and (first.remaining > 1 or len(parties) != 2):
            second = heapq.heappop(parties)
            current_step += second.name
            second.evacuate()
            if second.remaining > 0:
                heapq.heappush(parties, second)
        elif first.remaining - second.remaining > 1:
            current_step += first.name
            first.evacuate()

        first.evacuate()
        if first.remaining > 0:
            heapq.heappush(parties, first)

        plan.append(current_step)

    print "Case #{}: {}".format(case_number, " ".join(plan))
