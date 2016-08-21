__author__ = "Quy Doan"

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,"r") as reader:
    with open(output_file,"w") as writer:
        num_of_test = int(reader.readline())
        for test in range(num_of_test):
            k,c,s = map(int,reader.readline().split())
            res = [str(i+1) for i in range(s)]
            writer.write("Case #"+str(test+1)+": "+" ".join(res)+"\n")

