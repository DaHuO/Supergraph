"""
    Oh yeah
"""
from sets import Set

def count_sheep(input):
    """
    Returns last number before falling asleep
    """
    if input == 0:
        return "INSOMNIA"
    digit_set = Set([])
    for i in range(1,1000000):
        digit_set = digit_set.union(Set(str(i*input)))
        if len(digit_set) == 10:
            return str(i*input)
    return "INSOMNIA"

with open('A-large.in') as file:
    with open('output.raw' ,'w') as ofile:
        n = int(file.readline())
        i = 1
        for line in file:
            ofile.write('Case #{}: {}\n'.format(i, count_sheep(int(line))))
            i += 1
