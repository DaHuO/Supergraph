out = open("A.out", "w")
with open("A.in") as f:
    case_num = 1
    num_cases = int(f.readline())
    for line in f:
        N = int(line)
        if N == 0:
            out.write("Case #{}: INSOMNIA\n".format(case_num))
        else:
            seen = set(['0','1','2','3','4','5','6','7','8','9'])
            num_iterations = 1
            count = 0
            while seen:
                count = N * num_iterations
                for digit in str(count):
                    if digit in seen:
                        seen.remove(digit)
                num_iterations += 1
            out.write("Case #{}: {}\n".format(case_num, count))
        case_num += 1
out.close()