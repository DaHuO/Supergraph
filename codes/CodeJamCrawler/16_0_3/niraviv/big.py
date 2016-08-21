# A number that has all 0/1 digits in base b is composite if number of ones in even positions is
# equal to the number of ones in odd positions. In particular, b+1 is a divisor.

t = int(raw_input())
n, j = [int(s) for s in raw_input().split(" ")]
z = "1" + "0"*(n-2) + "1"
divisors = " 3 2 5 2 7 2 3 2 11"
print "Case #1:"
print z + divisors
m = n / 2
jamcoins_found = 1
for even_index1 in xrange(1, m):
    for even_index2 in xrange(even_index1 + 1, m):
        for odd_index1 in xrange(1,m):
            for odd_index2 in xrange(odd_index1 + 1, m):
                w = list(z)
                w[2 * even_index1] = '1'
                w[2 * even_index2] = '1'
                w[2 * odd_index1 - 1] = '1'
                w[2 * odd_index2 - 1] = '1'
                print "".join(w) + divisors
                jamcoins_found +=1
                if jamcoins_found == j:
                    exit()