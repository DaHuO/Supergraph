__author__ = "Quy Doan"

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
  
with open(input_file,"r") as reader:
    with open(output_file,"w") as writer:
        num_of_test = int(reader.readline())
        for test in range(num_of_test):
            cakes = reader.readline().strip()
            stack = [0 for x in range(len(cakes))]
            for i in range(len(stack)):
                if cakes[i] == '+':
                    stack[i] = 1
            print cakes,stack
            flips = 0
            while True:
                deep = 0
                for x in stack:
                    if x == stack[0]:
                        deep += 1
                    else:
                        break
                if stack[0] == 1 and deep == len(stack):
                    break
                flips += 1
                for i in range(deep):
                    stack[i] = 1 - stack[i]
            writer.write("Case #"+str(test+1)+": "+str(flips)+"\n")
