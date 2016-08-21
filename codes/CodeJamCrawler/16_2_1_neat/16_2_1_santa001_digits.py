num_str = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
           "SIX", "SEVEN", "EIGHT", "NINE"]

def is_present(string, num, pattern):
    if pattern not in string:
        return False
    for k in num_str[num]:
        string.pop(string.index(k))
    return True

if __name__ == "__main__":
    T = int(raw_input())

    for i in range(1, T+1):
        string = list(raw_input())
        num = []

        # Check for zero
        while is_present(string, 0, 'Z'):
            num.append(0)

        # Check for two
        while is_present(string, 2, 'W'):
            num.append(2)

        # Check for four
        while is_present(string, 4, 'U'):
            num.append(4)

        # Check for six
        while is_present(string, 6, 'X'):
            num.append(6)

        # Check for eight
        while is_present(string, 8, 'G'):
            num.append(8)

        # Check for one
        while is_present(string, 1,  'O'):
            num.append(1)

        # Check for one
        while is_present(string, 5,  'F'):
            num.append(5)

        # Check for one
        while is_present(string, 7,  'S'):
            num.append(7)

        # Check for one
        while is_present(string, 3,  'R'):
            num.append(3)

        # Check for one
        while is_present(string, 9,  'I'):
            num.append(9)

        num.sort()
        print "Case #%d: %s" %(i, "".join(map(str,num)))
