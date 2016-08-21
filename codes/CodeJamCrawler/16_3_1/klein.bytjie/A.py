fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']


def find_max_indices(a):
    m = max(a)
    return [i for i, j in enumerate(a) if j == m]


T = int(fin.readline())  # test cases
for i in range(T):
    # input parsing
    N = int(fin.readline())
    inside = map(int, fin.readline().split(" "))
    # inside = {}
    # for j,p in enumerate(P):
    #     inside[alphabet[j]] = p

    # algorithm
    result = []
    while any(inside):  # is not False
        max_idx = find_max_indices(inside)
        #print max_idx
        if len(max_idx) == 1:
            inside[max_idx[0]] -= 1
            result.append(alphabet[max_idx[0]])
        if len(max_idx) == 2:
            tmp_result = []
            for idx in max_idx:
                #print idx
                inside[idx] -= 1
                tmp_result.append(alphabet[idx])
            #print tmp_result
            result.append("".join(tmp_result))
        if len(max_idx) > 2:
            inside[max_idx[0]] -= 1
            result.append(alphabet[max_idx[0]])

    #print
    #print result
    formatted_result = " ".join(result)
    print >> fout, "Case #%d: %s" % (i+1, formatted_result)

fin.close()
fout.close()