import sys

# order in which we are going to check for a number
check_order = [('Z', 0, 'ZERO'),
               ('W', 2, 'TWO'),
               ('X', 6, 'SIX'),
               ('G', 8, 'EIGHT'),
               ('H', 3, 'THREE'),
               ('R', 4, 'FOUR'),
               ('S', 7, 'SEVEN'),
               ('V', 5, 'FIVE'),
               ('I', 9, 'NINE'),
               ('N', 1, 'ONE')]

def digits_left(freq_map):
    for i in freq_map:
        if freq_map[i] > 0:
            return True

    return False

def convert_num_freq_to_str(num_freq):
    number_str = ""

    for i in range(10):
        count_i = num_freq.get(i)
        if count_i != None:
            for j in range(count_i):
                number_str += str(i)

    return number_str

def phone_number(freq_map):
    number = { }

    for (l, n, word) in check_order:
        l_count = freq_map.get(l)

        if l_count != None:
            while l_count > 0:
                l_count -= 1
                if n in number:
                    number[n] += 1
                else:
                    number[n] = 1

                for w in word:
                    freq_map[w] -= 1

        if digits_left(freq_map) == False:
            return convert_num_freq_to_str(number)
    return

def main():
    num_tests = int(sys.stdin.readline())
    for tc in xrange(1, num_tests+1):
        S = raw_input()
        freq_map = { }
        for l in S:
            if l in freq_map:
                freq_map[l] += 1
            else:
                freq_map[l] = 1

        # dump the result
        print "Case #" + str(tc) + ": " + phone_number(freq_map)

    return

if __name__ == "__main__":
    main()
