import sys


def cs():
    with open(sys.argv[1], "r") as a_file, open(sys.argv[1] + "_output", "w") as out_file:
        test_cases = int(a_file.readline())
        for test_case in range(test_cases):
            N = int(a_file.readline())
            d = {str(x) for x in range(10)}
            val = "INSOMNIA"
            for i in range(1, 10000):
                digits = list(str(N*i))
                for t in digits:
                    if t in d:
                        d.remove(t)
                if len(d) == 0:
                    val = N*i
                    break
            out_file.write("Case #%d: %s\n" % (test_case+1, str(val)))
            print(val)
if __name__ == "__main__":
    cs()