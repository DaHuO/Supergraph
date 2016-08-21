def get_divisors(num_string):
    divisors = []

    for base in xrange(2, 11):
        num_base = int(num_string, base)

        divisor = get_divisor(num_base)
        if divisor != 0:
            divisors.append(divisor)
        else:
            return False

    return divisors

def get_divisor(x):
    for divisor in xrange(3, min(x, 100)):
        if x % divisor == 0:
            return divisor

    return 0

raw_input()
[N, J] = [int(x) for x in raw_input().split()]

print "Case #1:"

found = 0

start_string = s = '1' + '0' * (N - 2) + '1'
end_string = '1' * N

#for num in xrange(int(start_string, 2), int(end_string, 2) + 1, 2):

num = int(start_string, 2)
num_end = int(end_string, 2) + 1

while num < num_end:
    num_binary_string = "{0:b}".format(num)

    divisors = get_divisors(num_binary_string)
    if divisors:
        print num_binary_string, " ".join(str(x) for x in divisors)
        found += 1
        if found == J:
            break

    num += 2

