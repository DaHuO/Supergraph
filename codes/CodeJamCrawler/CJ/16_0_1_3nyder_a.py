def put_digits(string,number):
    number = str(number)
    for digit in number:
        if digit not in string:
            string += digit
    return string

t = int(raw_input())

for i in xrange(1, t + 1):

    n = int(raw_input())
    current_string = ""
    new_string = put_digits("", n)
    current_i = 1

    if n == n*2:
        print "Case #{}: INSOMNIA".format(i)
        continue

    while len(current_string) < 10:
        current_string = new_string
        current_i += 1
        new_string = put_digits(current_string, n*current_i)

    print "Case #{}: {}".format(i, n * (current_i-1))