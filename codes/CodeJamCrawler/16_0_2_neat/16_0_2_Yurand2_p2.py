import concurrent.futures
import os

NUM_THREADS = 1
def compute():
    n = int(raw_input())
    lines = [raw_input() for _ in xrange(n)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(algorithm, line) for line in lines]
        concurrent.futures.wait(futures)        
        for i, future in enumerate(futures, 1):
            print "Case #%d: %s" % (i, future.result())

def algorithm(line):
    if line.find("-") == -1:
        return 0
    
    current = line[0]
    cnt = 0
    for c in line:
        if c != current:
            cnt += 1
            current = c
    if current == "-":
        cnt += 1
    return cnt

compute()

