import fileinput


def get_solution(line):
    seen_numbers = set()
    seen_digits = set()
    base = int(line)
    number = base
    while True:
        for digit in str(number):
            seen_digits.add(digit)

        if len(seen_digits)==10:
            return number
        number += base
        if number in seen_numbers:
            return "INSOMNIA"
        seen_numbers.add(number)


if __name__ == '__main__':
    
    for (linenr, line) in enumerate(fileinput.input()):
        line = line.replace('\n', '')
        
        if fileinput.isfirstline():
            n = int(line)
            continue
        
        if linenr>n:
            print 'too many input lines (?)'
            break

        print 'Case #%d: %s' % (linenr, get_solution(line))

    
    
    
