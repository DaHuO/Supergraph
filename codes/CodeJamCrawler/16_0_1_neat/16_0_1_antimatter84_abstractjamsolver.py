#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AbstractJamSolver(object):
    def __init__(self, inputfile, outputfile):
        super(AbstractJamSolver, self).__init__()
        self._inputfile = inputfile
        self._outputfile = outputfile
        self._infile = None
        self._outfile = None
        
    def solve(self):
        self._infile = open(self._inputfile)
        self._outfile = open(self._outputfile, "wb")
        case_count = int(self._infile.readline())
        for c in range(case_count):
            result = self.solve_case()
            self._outfile.write("Case #%d: %s\n" % (c+1, result))
            print "Case #%d: %s" % (c+1, result)

    def solve_case(self):
        raise NotImplementedError
        