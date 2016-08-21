import os

case_num = 1

def final_number(n):
    if n == 0:
        return 'INSOMNIA'
    if n != 0:
        a = range(0, 10)
        digits_seen = []
        multiplier = 0
        while digits_seen != a:
            multiplier += 1
            n_string = str(n * multiplier)
            for i in range(0, len(n_string)):
                if int(n_string[i]) not in digits_seen:
                    digits_seen.append(int(n_string[i]))
                    digits_seen = sorted(digits_seen)
        return multiplier*n

            
with open('A-large.in', 'rb') as text_file:
    t = text_file.readline().strip('\r\n')
    for line in text_file:
        line = int(line.strip('\r\n'))
        print 'Case #%s: %s' % (case_num, final_number(line))
        case_num += 1

