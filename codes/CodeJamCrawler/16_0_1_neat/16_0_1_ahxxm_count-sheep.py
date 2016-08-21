# Count
import copy

t = int(input())
all_digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}


def iter_input():
    for i in range(1, t + 1):
        yield (i, int(input()))

#
def solve(integer: int, sequence: int) -> str:
    answer = integer
    seen_set = {char for char in str(integer)}
    if seen_set == all_digits:
        return answer

    start = 1
    while True:
        candi = integer * start
        candi_set = {char for char in str(candi)}
        #if seen_set.issuperset(candi_set):
            #answer = "INSOMNIA"
            #break

        seen_set.update(candi_set)
        if seen_set == all_digits:
            answer = candi
            break

        if start == 1000:
            answer = "INSOMNIA"
            break
        start += 1

    print("Case #{0}: {1}".format(sequence, answer))



if __name__ == "__main__":
    # python count-sheep.py < input.txt
    for seq, integer in iter_input():
        solve(integer, seq)
