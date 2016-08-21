#
# Source code file for Google Code Jam 2016 by user jdemeyer to solve
# problem A of Round 1A.
#
# This is a Cython file to be run with SageMath version 7.2.beta3 on a
# 64-bit GNU/Linux system. Note that the precise version of SageMath
# probably does not matter that much.
#
# To execute, enter a Sage shell with the command "sage --sh" and enter
# the following in the Sage shell:
#   python -c 'from setuptools import setup; from Cython.Build import cythonize; import Cython.Compiler.Options; from sage.env import sage_include_directories; Cython.Compiler.Options.embed="main"; setup(ext_modules=cythonize("R1A2016A.pyx"), include_dirs=sage_include_directories())' build_ext --inplace
#   ./R1A2016A.so input.in
# 
#distutils: extra_link_args = -pie -Wl,-E

from __future__ import print_function

import os, sys, datetime, time
from sage.all import Integer
include "cysignals/signals.pxi"


def log(msg):
    print(msg, file=sys.stderr)
    sys.stderr.flush()


class CodejamProblem(object):
    def __init__(self, input):
        self.inputlines = iter(input.splitlines())
        self.cases = []
    
    def readline(self):
        return next(self.inputlines)
        
    def readint(self):
        return Integer(self.readline())

    def readints(self):
        return [Integer(x) for x in self.readline().split()]
        
    def solve(self, f=sys.stdout, raw=False):
        for i, case in enumerate(self.cases, 1):
            sig_check()
            ans = self.solvecase(case)
            if raw:
                ans = repr(ans)
            else:
                ans = self.formatanswer(ans)
            f.write("Case #{0}: {1}\n".format(i, ans))
        f.flush()
        
    def solvecheck(self, output):
        from StringIO import StringIO
        out = StringIO()
        self.solve(out)
        assert out.getvalue() == output
            
    def formatanswer(self, ans):
        return str(ans)

    @classmethod
    def precompute(cls):
        pass
    
    @classmethod
    def autosolve(cls, filename, *args, **kwds):
        log("precomputing...")
        cls.precompute()

        log("autosolving...")

        nexc = 0
        while nexc < 10:
            sig_check()
            t0 = datetime.datetime.now()
            try:
                input = open(filename).read()
            except IOError:
                time.sleep(0.2)
                continue
            d = datetime.datetime.now() - t0
            log("Read input in %.2fs" % d.total_seconds())
            
            t0 = datetime.datetime.now()
            try:
                problem = cls(input, *args, **kwds)
            except Exception:
                from traceback import print_exc
                print_exc(file=sys.stderr)
                nexc += 1
                time.sleep(0.5)
                continue
            d = datetime.datetime.now() - t0
            ncases = len(problem.cases)
            log("Parsed input in %.2fs, got %s cases" % (d.total_seconds(), ncases))
            
            t0 = datetime.datetime.now()
            problem.solve()
            d = datetime.datetime.now() - t0
            log("Solved problem in %.2fs" % d.total_seconds())

            problem.notify()
            return
        
    @staticmethod
    def notify():
        os.system("mplayer /usr/share/apps/kgoldrunner/themes/default/victory.ogg >/dev/null")


class Problem(CodejamProblem):
    def __init__(self, input):
        CodejamProblem.__init__(self, input)
        
        T = self.readint()
        for i in range(T):
            self.cases.append(self.readline())
            
    def solvecase(self, case):
        last = ""
        for c in case:
            last = max(c + last, last + c)
        return last


if __name__ == "__main__":
    if len(sys.argv) != 2:
        log("Usage: {} inputfilename".format(sys.argv[0]))
        sys.exit(2)
    Problem.autosolve(sys.argv[1])
