import sys


def rop():
    with open(sys.argv[1], "r") as a_file, open(sys.argv[1] + "_output", "w") as out_file:
        test_cases = int(a_file.readline())
        for test_case in range(test_cases):
            st = a_file.readline().strip()
            s_list = list(st)

            def count_last_positive(dt):
                for i in range(len(dt)-1, -1, -1):
                    if dt[i] == "-":
                        return i
                return None

            def flip(l, end):
                for i in range(end+1):
                    if l[i] == "-":
                        l[i] = "+"
                    else:
                        l[i] = "-"

            total_count = 0
            while True:
                c = count_last_positive(s_list)
                if c is None:
                    out_file.write("Case #%d: %d\n" % (test_case+1, total_count))
                    break
                flip(s_list, c)
                total_count += 1
            print(st, count_last_positive(st))

if __name__ == '__main__':
    rop()