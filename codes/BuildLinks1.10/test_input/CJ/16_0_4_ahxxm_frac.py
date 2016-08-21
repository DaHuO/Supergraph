# Count
t = int(input())


def iter_input():
    for i in range(1, t + 1):
        yield (i, input())

#
def solve(sequence, string):
    k, c, s = string.split(" ")
    k, s = int(k), int(s)
    answer = [str(i) for i in range(1, k + 1)]
    if int(s) < int(k):
        answer = ["IMPOSSIBLE"]

    print("Case #{0}: {1}".format(sequence, " ".join(answer)))



if __name__ == "__main__":
    # python count-sheep.py < input.txt
    for seq, string in iter_input():
        solve(seq, string)
