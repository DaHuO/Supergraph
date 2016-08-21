#!/usr/bin/env python

def get_digits(value):
    return [int(d) for d in str(value)]

def find_last_value(start_value):
    if start_value == 0:
        return None

    ALL_DIGITS = range(10)
    value = start_value
    while True:
        digits = get_digits(value)
        NEW_ALL_DIGITS = list()
        for d in ALL_DIGITS:
            if d not in digits:
                NEW_ALL_DIGITS.append(d)
        if len(NEW_ALL_DIGITS) == 0:
            break
        ALL_DIGITS = NEW_ALL_DIGITS
        value += start_value
    return value

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as infile:
        _ = infile.readline()
        line_index = 0
        for line in infile:
            start_value = int(line.strip())
            last_value = find_last_value(start_value)
            line_index += 1
            if last_value is None:
                print 'Case #%d: INSOMNIA' % (line_index)
            else:
                print 'Case #%d: %s' % (line_index,last_value)

