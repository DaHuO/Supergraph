sample_input = """5
-
-+
+-
+++
--+-
"""

sample_output = """Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3
"""


def do_one(line):
    def process_one(prev_data, pancake):
        count, prev_pancake = prev_data
        if ((prev_pancake == '' and pancake == '+') or
                pancake == prev_pancake):
            return prev_data
        return (count + 1, pancake)

    return reduce(process_one, line[::-1], (0, ''))[0]
