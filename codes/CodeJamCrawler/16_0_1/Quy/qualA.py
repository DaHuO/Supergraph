__author__ = "Quy Doan"

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

def defrag_number(n):
    defrag  = []
    while n > 0:
        defrag.append(n % 10)
        n /= 10
    return defrag


with open(input_file,"r") as reader:
    with open(output_file,"w") as writer:
        num_of_test = int(reader.readline())
        for test in range(num_of_test):
            n = int(reader.readline())
            result = "INSOMNIA"
            if n > 0:
                seen = [False for x in range(10)]
                counter = 0
                result = n
                while(True):
                    for x in defrag_number(result):
                        if seen[x] == False:
                            counter += 1
                            seen[x] = True
                    if counter == 10:
                        break
                    result += n
            writer.write("Case #"+str(test+1)+": "+str(result)+"\n")



