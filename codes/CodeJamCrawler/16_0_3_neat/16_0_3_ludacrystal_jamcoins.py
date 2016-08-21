import math
import sys

class Coin:
    def __init__(self, value, example):
        self.value = value
        self.example = example

#gets counterexample
def getcounter(n):
     # 0 and 1 are not primes
    if n < 2:
        return n

    # 2 is the only even prime number
    if n == 2: 
        return -1

    # all other even numbers are not primes
    if n % 2 == 0:
        return n / 2

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(math.sqrt(n)), 2):
        if n % x == 0:
            return x

    return -1

#returns a string of examples, or an empty string
def getexamples(jamcode):
    #print("getting examples for " + jamcode)
    examples = ""

    #we check all bases 2 through 10
    for b in range(2, 11):
        n = int(jamcode, b) 
        #print(str(n) + " in base " + str(b))
        counter = getcounter(n)        

        #value is prime
        if counter == -1:
            #print("breaks at " + str(b))
            return ""

        #add to our examples
        examples = examples + " " + str(counter)

    #print(examples)
    return examples

def getsolutions(n, j):
    #print("getting " + str(j) + " solutions with max string " + str(n))

    #array of solutions
    solutions = []

    #smallest non-prime is 4
    if (n < 2):
        return solutions

    minnum = 0
    maxnum = int(math.pow(2, n - 1)) - 1

    for i in range(minnum, maxnum):
        middle = bin(i)[2:n]
        while len(middle) < n - 2:
                middle = "0" + middle

        jamcode = "1" + middle + "1"
        #print(jamcode)
        #found all possibilities
        if len(solutions) == j:
            return solutions

        examples = getexamples(jamcode)
        if examples != "":
            #print("appending " + jamcode)
            coin = Coin(jamcode, examples)
            solutions.append(coin)

    return solutions

def main():
    #print("reading " + sys.argv[1])
    f = open(sys.argv[1])

    t = int(f.readline())

    for i in range(1, t+1):
        line = f.readline().split()
        n = int(line[0])
        j = int(line[1])
        solutions = getsolutions(n, j)

        #four lines
        print("Case #" + str(i) + ":")

        for x in range(0, j):
            print (str(solutions[x].value) + " " + solutions[x].example)


main()
