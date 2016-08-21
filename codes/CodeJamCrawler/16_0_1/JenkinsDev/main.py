num_tests = int(raw_input())
expected_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

def check_if_edge_case(inp):
    if inp == 0:
        return "INSOMNIA"
    elif inp == 1:
        return inp * 10
    return False

for i in range(1, num_tests + 1):
    inp = int(raw_input())
    val = check_if_edge_case(inp) or 0
    if not val:
        found = [l for l in str(inp)]
        j = 2
        while not set(found) == expected_set:
            product = inp * j
            found += [l for l in str(product)]
            j += 1
            if j > 1000:
                break
        val = product
    print("Case #%s: %s" % (i, val))
