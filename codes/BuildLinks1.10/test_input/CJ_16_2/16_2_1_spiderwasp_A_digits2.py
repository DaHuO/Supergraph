
import heapq

DIGIWORDS = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
}

class State(object):
    def __init__(self, text, digits=[]):
        # Force strings into list context. Also makes a copy
        self.text = list(text)
        self.digits = list(digits)

    def __str__(self):
        return "n={0} t={1}".format(self.ans(), ''.join(self.text))

    def ans(self):
        """Format the answer"""
        return ''.join([str(i) for i in sorted(self.digits)])

    def f(self):
        """Total cost (estimated)"""
        return self.g() + self.h()

    def g(self):
        """Cost so far"""
        return len(self.digits)

    def h(self):
        """Estimate cost left"""
        return len(self.text)

    def search(self):
        for digi, word in DIGIWORDS.iteritems():
            text_left = self.text[:]
            found_all = True
            for letter in word:
                if letter in text_left:
                    text_left.remove(letter)
                else:
                    found_all = False
                    break
            if found_all:
                new_found = self.digits[:]
                new_found.append(digi)
                yield State(text_left, new_found)
        self.searched = True

def solve(start):
    # push the start item onto the heapq. initial priority is unimportant, because only one item.
    searchq = [(0, State(start))]
    searched = []
    while len(searchq):
        cost, state = heapq.heappop(searchq)
        searched.append(state)
        # print cost, board
        for new_state in state.search():
            if new_state.h() == 0:
                # solved
                return new_state.ans()
            heapq.heappush(searchq, (new_state.f(), new_state))

def main():
    num_cases = int(raw_input())
    for case_id in range(num_cases):
        text = raw_input()
        ans = solve(text)
        print("Case #{0}: {1}".format(case_id + 1, ans))

if __name__ == "__main__":
    main()
