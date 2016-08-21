import fileinput
import collections
cases = 0
arrs = []
# count = {}
case_size = []
ans = []
for line in fileinput.input():
    if fileinput.isfirstline():
        cases = int(line)
    else:
        if line.find(' ') == -1:
            case_size.append(int(line))
        else:
            arrs.append(line.split())

ranges = [(0,2*case_size[0]-1)]
for i in range(1,len(case_size)):
    ranges.append((ranges[i-1][1], 2*case_size[i]+ranges[i-1][1]-1))
itr = 0
print(ranges)
for size in case_size:
    arr = [x for x in arrs[ranges[itr][0]:ranges[itr][1]]]
    # print(arr)
    itr += 1
    flat = [n for row in arr for n in row]
    count = collections.defaultdict(str)
    # print(flat)
    for i in flat:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # print(count)
    tmp_ans = []
    for k,v in count.iteritems():
        if v%2 != 0:
            tmp_ans.append(k)
    tmp_ans = [int(i) for i in tmp_ans]
    tmp_ans.sort()
    ans.append(" ".join(str(x) for x in tmp_ans))

f = open('output', 'w')
for i, a in enumerate(ans):
    f.write("Case #%i: %s" % ((i+1), a))
    f.write('\n')
f.close
