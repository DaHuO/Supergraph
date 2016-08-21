from collections import defaultdict
import sys


def solve(A):
    M = len(A)
    N = (M+1)/2
    diags = []
    missing_i = 0
    for i in xrange(N):
      diag_j = defaultdict(list)
      diag_i = []
      for j in xrange(M):
        diag_i.append(A[j][i])
        diag_i.sort()
        diag_j[A[j][i]].append(j)
      i_min = diag_i[2*i]
      diags.append((i_min, diag_j[i_min]))
      if len(diag_j[i_min]) < 2:
        missing_i = i

    ret = [0]*N
    ret[missing_i] = diags[missing_i][0]
    i_counter = diags[missing_i][1][0]
    for i in xrange(N):
        if i != missing_i:
            a, b = diags[i][1]
            pos_i = [A[a][missing_i], A[b][missing_i]]
            pos_i.remove(A[i_counter][i])
            ret[i] = pos_i[0]
    # print diags, missing_i, ret
    return " ".join(map(str, ret))


if __name__ == "__main__":
    output_file = open("%s.%s" % (sys.argv[1].split(".")[0], "out"), "w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        N = int(input_file.readline().strip())
        M = 2*N - 1
        A = [[0]*N]*M
        for j in xrange(M):
            A[j] = map(int, input_file.readline().split())
        # print pancakes
        result = solve(A)
        output_file.write("Case #%s: %s\n" % (i+1, result))

    output_file.close()
    input_file.close()
    print "Done!"
