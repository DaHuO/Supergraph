import sys


input_data = open(sys.argv[1])
filename = ".".join(sys.argv[1].split(".")[:-1])
def readline():
    return input_data.readline().rstrip()

def ind2letter(ind):
    return chr(ind+97).upper()

output_data = open(filename + ".out","w")

num_tests = int(readline())


# for i in range(1):
for test_ind in range(1,num_tests+1):
    _num_parties = int(readline())
    congress = [(ind2letter(ind), int(count)) for ind, count in enumerate(readline().split(' '))]
    congress = sorted(congress, key = lambda x:-x[1])
    total = sum([party[1] for party in congress])
    print 'congress: ', congress, ' total:', total
    output_data.write("Case #%s:" % test_ind)
    while True:
        if total == 0:
            output_data.write("\n")
            break
        congress = sorted(congress, key = lambda x:-x[1])
        if congress[0][1]==congress[1][1] and total != 3:
            # remove two of them
            congress[0] = (congress[0][0], congress[0][1] -1)
            congress[1] = (congress[1][0], congress[1][1] -1)
            output_data.write(" %s%s" % (congress[0][0],congress[1][0]))
            total -= 2
        else:
            # remove one
            congress[0] = (congress[0][0], congress[0][1] -1)
            output_data.write(" %s" % congress[0][0])
            total -= 1

