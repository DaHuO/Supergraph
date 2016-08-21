import math
filename = "D-large"


with open(filename + ".in", "r") as input:
    with open(filename + ".out", "w") as output:
        for case_num in range(1, int(input.readline()) + 1):
            output.write("Case #{}:".format(case_num))
            values = input.readline()
            list_val = values.split()
            k = int(list_val[0])
            c = int(list_val[1])
            s = int(list_val[2])
            if math.ceil(k / c) > s:
                output.write(" IMPOSSIBLE\n")
            else:
                i = 0
                while i < k:
                    acc = 1
                    for j in reversed(range(c)):
                        acc += min(i, k-1) * (k**j)
                        i += 1
                    output.write(" " + str(acc))
                output.write("\n")
