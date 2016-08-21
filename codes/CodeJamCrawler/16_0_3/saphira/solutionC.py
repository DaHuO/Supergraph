import time
import itertools
import logging
logger = logging.getLogger('test')
logging.basicConfig(filename="test.log")


def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_ouput():
    lines = getInput("inputC.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while case <= no_cases:
        N = int(lines[case].strip().split()[0])
        J = int(lines[case].strip().split()[1])
        print "Case #{0}:".format(case)
        get_solution(N, J)
        case += 1


def get_solution(N, J):
    bases = [x for x in xrange(2, 11)]
    done_count = 0
    for i in itertools.product(['0', '1'], repeat=N-2):
        if done_count >= J:
            break
        curr_num = '1' + ''.join(i) + '1'
        curr_num_map = {}
        prime = False
        for base in bases:
            curr_num_map[base] = {"num": int(curr_num, base)}
            #stime = time.time()
            prime_check, curr_num_map[base]["div"] = isprime(curr_num_map[base]["num"])
            #logger.critical("Tested {0} {1}".format(curr_num_map[base]["num"], time.time()-stime))
            if prime_check is True:
                prime = True
                break
        if prime is False:
            print "{0} {1}".format(curr_num, ' '.join([str(curr_num_map[x]["div"]) for x in curr_num_map]))
            done_count += 1
            logger.critical("Found Number: {0}".format(done_count))


def isprime(n):
    if n == 2:
        return True, None
    if n == 3:
        return True, None
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3
    i = 5
    w = 2
    total_checks = 0
    while i * i <= n and total_checks <= 100000:
        #print "Checking", i, total_checks
        if n % i == 0:
            return False, i
        total_checks += 1
        i += w
        w = 6 - w
    return True, None

print_ouput()
#isprime(1326443518324400147398873)