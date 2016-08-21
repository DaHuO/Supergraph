from code_jam import *

@autosolve
@collects
def solve(tokens):
    done = set()
    input = tokens.next_token(int)

    current = input
    for i in range(10000):
        for char in str(current):
            done.add(char)
        if len(done) == 10:
            return current
        current += input
    return "Insomnia"