#!/usr/bin/python2

import random

def bucket_sort(A, num_buckets, debug=False):
    """Bucket sort an array with num_buckets"""
    min_ = min(A)
    max_ = max(A)
    B = [[] for i in range(num_buckets)]
    for e in A:
        i = int((e - min_)/(max_ - min_) * (num_buckets - 1))
        B[i].append(e)
    for i in range(len(B)):
        B[i] = sorted(B[i]) 
    if debug:
        print "Buckets:"
        for b in B:
            print b
    return reduce(lambda x, y: x + y, B)
    

if __name__ == "__main__":
    N = 100
    A = [random.uniform(0, 1) for i in range(N)]
    bucket_sort(A, 100, debug=True)
    
