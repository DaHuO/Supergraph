#!/usr/bin/env python

# A.py


from __future__ import print_function
import sys

DEBUG = True


input_data = open(sys.argv[1])
filename, _ = sys.argv[1].split(".")
output = open(filename + ".out","w")

num_tests = int(input_data.readline().rstrip())
for tt in range(1,num_tests+1):
    K, C, _ = [int(x) for x in input_data.readline().rstrip().split()]
    cluster_size = K**(C-1)
    result = " ".join([str(i*cluster_size + 1) for i in range(K)])
    print("K= ", K)
    print("C=",C)
    print("samples=",result)
    output.write("Case #%s: %s\n" %(tt, result))
    # import pdb; pdb.set_trace()
    # output_data.write("Case #%s: %s\n" % (i, solver(N)))
