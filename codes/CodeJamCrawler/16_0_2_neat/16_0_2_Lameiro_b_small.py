def flip_str(s, i):
    r = []
    for char in reversed(s[:i]):
        if char == '-':
            r.append('+')
        else:
            r.append('-')

    r.append(s[i:])
    return ''.join(r)

def solve(s):
    queue = [(s, 0)]
    nodes_added = {s}

    while True:
        node_string, node_cost = queue[0]
        del queue[0]

        if node_string.count('-') == 0:
            return node_cost

        new_cost = node_cost + 1
        for i in xrange(1, len(node_string)+1):
            new_string = flip_str(node_string, i)

            if new_string not in nodes_added:
                queue.append((new_string, new_cost))
                nodes_added.add(new_string)

number_of_cases = int(raw_input())
for case_number in xrange(1, number_of_cases+1):
    s = raw_input()
    result = solve(s)

    print "Case #%d: %s" % (case_number, result)
    case_number += 1

# print solve('-')
# print solve('-+')
# print solve('+-')
# print solve('+++')
# print solve('--+-')
# print solve('----------')


# import time
#
# start = time.time()
# print solve('-----+-+-+-+-+++-')
# print time.time()-start