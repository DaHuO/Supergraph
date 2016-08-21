# print('sheep counter...')

input_file = 'A0small.in'

first_line = True

count = -1

for line in open(input_file, 'r'):
    count += 1
    if first_line:
        num_tests = int(line)
        first_line = False
    else:
        base = int(line)

        digits = '0123456789'

        max_limit = 1000000

        for i in xrange(1,1000000):
            integer = i*base
            string = str(integer)
            # print('string: %s' % (string,))
            for j in xrange(0,len(digits)):
                if j >= len(digits):
                    break
                if digits[j] in string:
                    # print('found %s' % (digits[j]))
                    digits = digits[:j] + digits[j+1:]

            for j in xrange(0,len(digits)):
                if j >= len(digits):
                    break
                if digits[j] in string:
                    # print('found %s' % (digits[j]))
                    digits = digits[:j] + digits[j+1:]

            if len(digits) <= 0:
                print('Case #%d: %s' % (count, string,))
                break
            elif i == max_limit-1:
                print('Case #%d: INSOMNIA' % (count,))