import concurrent.futures
import os

NUM_THREADS = 8
def compute():
    n = int(raw_input())
    lines = [raw_input() for _ in xrange(n)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(algorithm, line) for line in lines]
        concurrent.futures.wait(futures)        
        for i, future in enumerate(futures, 1):
            print "Case #%d: %s" % (i, future.result())

def algorithm(line):
    left = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    N = str(line)
    if N == "0":
        return "INSOMNIA"
    
    k = 1L
    while 1:
        numbers = set()
        for digit in str(k * int(N)):
            numbers.add(digit)
        for number in list(left):
            if number in numbers:
                left.remove(number)
        if len(left) == 0:
            break
        k = k + 1
    return str(k * int(N))

compute()
        
