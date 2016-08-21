# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def countingSheep(n):

    allDigits = ["1","2","3","4","5","6","7","8","9","0"]
    res = []

    res.append(str(n))
    counter = 1

    finalN = 0

    if n == 0:
        return "INSOMNIA"

    while not set(allDigits).issubset(set(res)):
        finalN = n * counter
        stringN = str(finalN)

        for digit in stringN:
            res.append(digit)

        counter += 1

    return finalN


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input()) # read a list of integers, 2 in this case
  print  "Case #{}: {}".format(i,countingSheep(n))
  # check out .format's specification for more formatting options