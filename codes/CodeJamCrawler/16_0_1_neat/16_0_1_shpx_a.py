name = "A-large"

with open(name+'.in', 'r') as f:
    f.readline()
    for i, line in enumerate(f):
        number = int(line)
        cur_number = number

        digits = set(list(str(cur_number)))
        x = 0
        while x < 500:
            cur_number += number
            digits.update(set(list(str(cur_number))))
            x += 1
            if len(digits) == 10:
                print "Case #{}: {}".format(i+1, cur_number)
                break
        else:
            print "Case #{}: INSOMNIA".format(i+1)


