from __future__ import division

import os

from Tools import gcj


#from Tools import primes


def solver(n):
    digits = set()
    if n == 0:
        return 'INSOMNIA'

    i = 1
    while len(digits) < 10:
        v = i * n
        for c in str(v):
            digits.add(c)
        if len(digits) == 10:
            return v
        i+=1
    return n

def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    n = in_file.getInt()

    return {
        'n': n
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
