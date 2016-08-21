import sys

def main(input_file):
    with open(input_file) as f:
        tc = f.readlines()
    required_tc_num = tc.pop(0)

    for tc_num, pancakes in enumerate(tc):
        ans = get_num_flips(pancakes.strip())
        print 'Case #%d: %s' % (tc_num + 1, ans)

def get_num_flips(pancakes):
    curr_state = "+"
    ret = 0
    for i in reversed(pancakes):
        if i != curr_state:
            ret += 1
            curr_state = "+" if curr_state == "-" else "-"
        elif i == "+":
            continue
    return ret

if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
