from __future__ import division

import os

from Tools import gcj
import re

def solver(s):
    s = re.sub("[-]+", "-", s)
    s = re.sub("[+]+", "+", s)
    if s[0] == '-' and len(s) % 2 == 0:
        return len(s) - 1
    elif s[0] == '-' and len(s) % 2 != 0:
        return len(s)
    elif s[0] == '+' and len(s) % 2 != 0:
        return len(s) - 1
    else:
        return len(s)


def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    s = in_file.readline()

    return {
        's': s
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
