import sys
import time
from datetime import datetime
from multiprocessing import Pool


def solver(data):
    index = data[0]
    number = int(data[1])
    if number:
        current_number = 0
        number_pool = set()
        while len(number_pool) != 10:
            current_number += number
            number_pool.update(set(list(str(current_number))))
        return "Case #%s: %s" % (index, current_number)
    else:
        return "Case #%s: INSOMNIA" % index


pool = Pool()
output_path = 'outputs/%s.txt' % time.time()
input_file = open(sys.argv[1], 'r')
output_file = open(output_path, 'w')

print "======= Start ======="
start_time = datetime.now()

limit = int(input_file.readline().strip())
inputs = map(lambda (index, line): (index+1, line.strip()), enumerate(input_file.readlines()))
results = pool.map(solver, inputs)

output_file.write("\n".join(results))

print "Output to %s" % output_path
print "Take time : %s" % (datetime.now() - start_time)
print "======= Finish ======="
