import operator
from itertools import imap

def print_case(case_no, answer):
    print 'Case #{case_no}: {answer}' \
        .format(
            case_no = case_no,
            answer = answer
        )

class Evacuator():
    def __init__(self, case, parties):
        self.case = case
        self.start_party = 'A'
        self.parties = {}

        for i, x in enumerate(parties):
            self.parties[chr(ord(self.start_party) + i)] = int(x)

    def create_plan(self):
        result = []

        while self.get_total_remaining() > 0:
            if self.get_total_remaining() == 3 and \
               self.get_total_parties() == 3:
                senates = self.select_one()
            else:
                senates = self.select_two()

            self.evalucate(senates[0])

            if len(senates) > 1: self.evalucate(senates[1])
            result.append(senates)

        print_case(self.case, ' '.join(result))

    def select_one(self):
        return self.get_max_parties(1)[0][0]

    def select_two(self):
        ps = self.get_max_parties(2)

        if ps[0][1] - 1 > ps[1][1]:
            result = ps[0][0] * 2
        else:
            result = ps[0][0] + ps[1][0]

        return result

    def evalucate(self, party):
        self.parties[party] -= 1
        if self.parties[party] == 0:
            self.parties.pop(party)

    def get_total_remaining(self):
        return sum(self.parties.itervalues())

    def get_total_parties(self):
        return len(self.parties.keys())

    def get_max_parties(self, n=2):
        return sorted(self.parties.iteritems(), key=operator.itemgetter(1), reverse=True)[:n]

if __name__ == '__main__':
    total = int(raw_input())

    for i in xrange(1, total+1):
        party_count = raw_input()
        Evacuator(i, raw_input().split(' ')).create_plan()
