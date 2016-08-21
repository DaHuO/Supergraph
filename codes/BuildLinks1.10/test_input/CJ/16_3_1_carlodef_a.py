def who_are_the_first_out(senators):
    if sum(senators) < 3:
        kk = []
        while sum(senators):
            p = senators.index(max(senators))
            senators[p] -= 1
            kk.append(p)
        return ''.join([chr(ord('A') + x) for x in kk])

    number_of_senators_in_the_biggest_party = max(senators)
    biggest_party = senators.index(number_of_senators_in_the_biggest_party)
    #print "biggest party: %s" % chr(ord('A') + biggest_party)
    out = chr(ord('A') + biggest_party)
    senators[biggest_party] -= 1

    number_of_senators_in_the_biggest_party = max(senators)
    biggest_party = senators.index(number_of_senators_in_the_biggest_party)
    #print "biggest party: %s" % chr(ord('A') + biggest_party)
    senators[biggest_party] -= 1
    if max(senators) <= 0.5 * sum(senators):
        out = "%s%s" % (out, chr(ord('A') + biggest_party))
    else:
        senators[biggest_party] += 1
    return out


def solve(senators):
    out = []
    while sum(senators):
        out.append(who_are_the_first_out(senators))
    return out


if __name__ == '__main__':
    T = int(raw_input())
    for test in xrange(T):
        N = int(raw_input())
        senators = map(int, raw_input().split())
        assert(len(senators) == N)
        print "Case #%d: %s" % (test+1, ' '.join(solve(senators)))
