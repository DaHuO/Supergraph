import sys
from subprocess import Popen, PIPE
from concurrent.futures import ThreadPoolExecutor

max_iterations = 1000000

fp = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")

total = int(fp.readline())



case = 0



for num in fp:
    case = case + 1

    N = int(num)
    flag = False
    tracker = {}

    for i in range(1, max_iterations):
        curr_num = N * i
        for char in list(str(curr_num)):
            if int(char) in range(0, 10):
                tracker[int(char)] = True

        flag = False
        for d in range(0, 10):
            if d in tracker and tracker[d]:
                flag = True
            else:
                flag = False
                break
        if flag:
            break
    if flag:
        output.write("Case #{}: {}\n".format(case, curr_num))
    else:
        output.write("Case #{}: INSOMNIA\n".format(case))

fp.close()
output.close()
