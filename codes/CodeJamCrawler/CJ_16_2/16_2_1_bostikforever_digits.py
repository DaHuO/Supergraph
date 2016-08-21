import sys
from collections import Counter, defaultdict


def digits(number):
    count = Counter(number)
    count = defaultdict(int, count)
    dcount = {}
    dcount[0] = count['Z']
    dcount[2] = count['W']
    dcount[6] = count['X']
    dcount[7] = count['S'] - dcount[6]
    dcount[5] = count['V'] - dcount[7]
    dcount[4] = count['F'] - dcount[5]
    dcount[3] = count['R'] - dcount[0] - dcount[4]
    dcount[8] = count['H'] - dcount[3]
    dcount[9] = count['I'] - dcount[6] - dcount[8] - dcount[5]
    dcount[1] = count['N'] - dcount[7] - 2*dcount[9]

    ret = sorted(str(v)*c for v,c in dcount.items())
    return "".join(ret)
if __name__ == "__main__":
    output_file = open("%s.%s" % (sys.argv[1].split(".")[0], "out"), "w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        number = input_file.readline().strip()
        # print pancakes
        result = digits(number)
        output_file.write("Case #%s: %s\n" % (i+1, result))

    output_file.close()
    input_file.close()
    print "Done!"
