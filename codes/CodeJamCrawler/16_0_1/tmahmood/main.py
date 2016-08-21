#!/bin/python


def says_all_digits(multiplier):
    """goes through all the digits

    :multiplier: @todo
    :returns: @todo

    """
    steps = 1
    digits_seen = [0] * 10
    last_value = 0
    continued = 0
    while True:
        new_value = multiplier * steps
        if new_value == last_value:
            continued += 1
            if continued > 50:
                break
            else:
                continue
        continued = 0
        last_value = new_value
        result = "%s" % new_value
        int_result = [int(m) for m in result]
        for k in int_result:
            digits_seen[k] = 1
        sum_of_digits_seen = sum(digits_seen)
        if sum_of_digits_seen == 10:
            return result
        steps += 1
    return False


def main():
    """
    main
    """
    how_many = int(input())
    for i in range(1, how_many + 1):
        multiplier = int(input())
        rep = says_all_digits(multiplier)
        if not rep:
            print("Case #%s: INSOMNIA" % i)
        else:
            print("Case #%s: %s" % (i, rep))


def test():
    """do testing
    :returns: @todo

    """
    print("%s\n" % says_all_digits(1692))
    print("%s\n" % says_all_digits(1))
    print("%s\n" % says_all_digits(11))
    print("%s\n" % says_all_digits(2))
    print("%s\n" % says_all_digits(0))

if __name__ == '__main__':
    main()
