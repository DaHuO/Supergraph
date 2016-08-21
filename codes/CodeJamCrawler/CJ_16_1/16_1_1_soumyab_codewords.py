import sys

sys.setrecursionlimit(5000)

T = int(raw_input())

# string is an array of letters that represent the codeword
def produce_codeword(string):
    if len(string) == 1:
        return string[0]
    elif len(string) == 0:
        return ''

    max_letter = max(string)

    next_index = len(string) - string[::-1].index(max_letter) - 1

    prefix = produce_codeword(string[:next_index])
    suffix = "".join(string[next_index+1:])

    return max_letter + prefix + suffix

for i in range(T):
    initial = str(raw_input())
    
    print ("Case #{0}: {1}".format(i+1, produce_codeword(initial)))
