filename = "A-large"

def contains_all_dig(set):
    if (len(set) == 10):
        return True
    else:
        return False


with open(filename + ".in", "r") as input:
    with open(filename + ".out.txt", "w") as output:
        for case_num in range(1, int(input.readline()) + 1) :
            output.write("Case #{}: ".format(case_num))
            starting_N = int(input.readline())
            if starting_N == 0:
                output.write("INSOMNIA\n")
            else:
                N = starting_N
                digit_set = set()
                while (not contains_all_dig(digit_set)):
                    for char in str(N):
                        digit_set.add(char)
                    N += starting_N
                output.write("{}\n".format(N - starting_N))
