import sys
all_seen_digits = [0] * 10

def main(input_file):
    with open(input_file) as f:
        tc = f.readlines()
    required_tc_num = tc.pop(0)

    for tc_num, num in enumerate(tc):
        global all_seen_digits
        all_seen_digits = [0] * 10
        num = num.strip()
        if num == '0':
            ans = 'INSOMNIA'
        else:
            last_num = get_last_num(num)
            ans = last_num
        print 'Case #%d: %s' % (tc_num + 1, ans)

def get_last_num(num, multi = 1):
    last_num = int(num) * multi
    mark_seen_digits(last_num)
    if are_all_digits_seen():
        return last_num
    else:
        return get_last_num(num,  multi + 1)

def are_all_digits_seen():
    return all(all_seen_digits)

def mark_seen_digits(num):
    for char in list(str(num)):
        all_seen_digits[int(char)] = 1

if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
