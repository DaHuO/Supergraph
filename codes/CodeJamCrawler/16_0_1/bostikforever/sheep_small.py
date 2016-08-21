import sys
from collections import Counter
def count_sheep(num):
    digits = len(str(num))
    N = 10 ** (digits + 1)
    # print N, num
    seen = Counter({'0':0, '1':0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8':0, '9':0})
    for i in xrange(1, N):
        k = i * num
        seen.update(str(k))
        # print seen
        if min(seen.values()) > 0:
            return k
    return "INSOMNIA"


if __name__ == "__main__":
    output_file = open("%s.%s" % (sys.argv[1].split(".")[0], "out"), "w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        number = int(input_file.readline().strip())
        # print pancakes
        result = count_sheep(number)
        output_file.write("Case #%s: %s\n" % (i+1, result))

    output_file.close()
    input_file.close()
    print "Done!"
