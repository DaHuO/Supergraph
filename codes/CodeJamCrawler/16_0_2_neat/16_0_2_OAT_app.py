import sys
from datetime import datetime
from multiprocessing import Pool
sys.setrecursionlimit(10000)
CANNOT_PROCESS_VALUE = 99999999


class FoundPerfectPancake(Exception):
    def __init__(self, move):
        self.move = move


def is_perfect(pancakes):
    return '-' not in pancakes


def move_plus(move, pancakes):
    move += 1
    try:
        index = pancakes.index('+')
        if not index:
            return CANNOT_PROCESS_VALUE
        sub_pancakes_reversed = pancakes[:index][::-1]
        new_sub_pancakes = ''.join(map(lambda pancake: '-' if pancake == '+' else '+', sub_pancakes_reversed))
        pancakes = new_sub_pancakes + pancakes[index:]
    except ValueError:
        return CANNOT_PROCESS_VALUE

    # print "Move Plus, Dept:%s Results:%s" % (move, pancakes)
    if is_perfect(pancakes):
        raise FoundPerfectPancake(move)
    return min(move_plus(move, pancakes), move_minus(move, pancakes), move_flip(move, pancakes))


def move_minus(move, pancakes):
    move += 1
    try:
        index = pancakes.index('-')
        if not index:
            return CANNOT_PROCESS_VALUE
        sub_pancakes_reversed = pancakes[:index][::-1]
        new_sub_pancakes = ''.join(map(lambda pancake: '-' if pancake == '+' else '+', sub_pancakes_reversed))
        pancakes = new_sub_pancakes + pancakes[index:]
    except ValueError:
        return 99999999

    # print "Move Minus, Dept:%s Results:%s" % (move, pancakes)
    if is_perfect(pancakes):
        raise FoundPerfectPancake(move)
    return min(move_plus(move, pancakes), move_minus(move, pancakes), move_flip(move, pancakes))


def move_flip(move, pancakes):
    move += 1
    pancakes = pancakes[::-1]
    pancakes = ''.join(map(lambda pancake: '-' if pancake == '+' else '+', pancakes))

    # print "Move Flip, Dept:%s Results:%s" % (move, pancakes)
    if is_perfect(pancakes):
        raise FoundPerfectPancake(move)
    return min(move_plus(move, pancakes), move_minus(move, pancakes), move_flip(move, pancakes))


def solver(data):
    index = data[0]
    pancakes = data[1]
    try:
        if is_perfect(pancakes):
            raise FoundPerfectPancake(0)
        min(move_plus(0, pancakes), move_minus(0, pancakes), move_flip(0, pancakes))
    except FoundPerfectPancake as perfect_pancake:
        result = "Case #%s: %s" % (index, perfect_pancake.move)
        return result


pool = Pool()
output_path = 'outputs/%s.out' % sys.argv[1].split('/')[-1].split('.')[0]
input_file = open(sys.argv[1], 'r')

print "======= Start ======="
start_time = datetime.now()

limit = int(input_file.readline().strip())
inputs = map(lambda (index, line): (index + 1, line.strip()), enumerate(input_file.readlines()))

# solver(inputs[4])
results = pool.map(solver, inputs)
output_file = open(output_path, 'w')
output_file.write("\n".join(results))

print "Output to %s" % output_path
print "Take time : %s" % (datetime.now() - start_time)
print "======= Finish ======="
