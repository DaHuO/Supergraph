import problem

SAMPLE = """7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
"""


class Solution(problem.Problem):

    def solve(self, case):
        whiteboard = ''
        for letter in case:
            if not whiteboard or letter >= whiteboard[0]:
                whiteboard = letter + whiteboard
            else:
                whiteboard = whiteboard + letter
        return whiteboard

    def parse_case(self, lines):
        return lines.next().strip()


if __name__ == '__main__':
    # Solution.run_sample(SAMPLE)
    Solution.run()
