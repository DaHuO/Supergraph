import sys
sys.setrecursionlimit(100000)


def index_of_largest_char(S):
    largest_letter = max(S)
    index = len(S) - 1

    while S[index] != largest_letter:
        index -= 1

    return index


def compute_last_word(S):
    if len(S) <= 2:
        return sorted([S, S[::-1]])[-1]

    index = index_of_largest_char(S)
    letter = S[index]

    first_part = S[:index]
    second_part = S[index+1:]
    return str(letter) + str(compute_last_word(first_part)) + str(second_part)



if __name__ == '__main__':
    with open('A-large.in', 'r') as input, open('A-large.xili.out', 'w') as output:
    # with open('A-small.in', 'r') as input, open('A-small.out', 'w') as output:
        num = int(input.readline())
        for case in range(num):
            S = input.readline().strip()
            last_word = compute_last_word(S)
            output_line = "Case #{num}: {last_word}\n".format(
                num=case + 1,
                last_word=last_word
            )
            # print output_line
            output.write(output_line)
