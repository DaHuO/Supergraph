cases = int(raw_input())

for case in range(cases):
    seen_numbers = ""
    number = raw_input()
    if number == '0':
        print "Case #%d: INSOMNIA" % (case + 1)
    else:
        counter = 2
        result = number
        while True:
            for digit in result:
                if digit not in seen_numbers:
                    seen_numbers += digit
            if ''.join(sorted(seen_numbers)) == "0123456789":
                print "Case #%d: %d" % (case + 1, int(result))
                break
            else:
                result = str(int(number) * counter)
                counter += 1
