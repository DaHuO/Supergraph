import fileinput
import math

i = 0
num_cases = -1
for line in fileinput.input():
    if (i == 0):
        num_cases = int(line)
    else:
        nums = line.split()
        k = int(nums[0])
        c = int(nums[1])
        s = int(nums[2])

        result = []

        if k == 1:
            if s >= 1:
                result.append(1)
        elif c == 1:
            if s>=k:
                for j in range(k):
                    result.append(j+1)
        elif s>=k:
            for j in range(k):
                result.append(j+1)
        else:
            num_needed = int(math.ceil(k/2.0))
            if s >= num_needed:
                section_length = int(math.pow(k, c-1))
                added = 0
                last_pos = 2
                while added < num_needed:
                    if added == 0:
                        result.append(last_pos)
                    else:
                        last_pos += section_length*2 + 2
                        if (last_pos) > math.pow(k, c):
                            last_pos = int(math.pow(k,c))
                        result.append(last_pos)
                    added+=1



        if len(result) > 0:
            to_print = "Case #" + str(i) + ":"       
            for num in result:
                to_print += " " + str(num)
            print to_print
        else:
            print "Case #" + str(i) + ": IMPOSSIBLE"
        

    i+=1
    if (i > num_cases):
        break