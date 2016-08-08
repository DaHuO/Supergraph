#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ast

class pythonast:
    def __init__(self, file_path):
        ffile = open(file_path, 'r')
        self.parse(ffile)

    def parse(self, ffile):
        
        fcode = ffile.read()
        funcs = []
        try:
            expr_ast = ast.parse(fcode)
            functions = []
            for i in expr_ast.body:
                if type(i).__name__ == 'FunctionDef':
                    functions.append(i)
            for i in functions:
                funcs.append((i.lineno, self.getfunclastline(i.body)))
        except Exception, e:
            print Exception,":",e
        print funcs
        return funcs

    def getfunclastline(self, funcbody):
        x = funcbody[-1]
        if 'orelse' in x._fields:
            return self.getfunclastline(x.body)
        elif 'body' in x._fields:
            return self.getfunclastline(x.body)
        else:
            return x.lineno

    def finished(self):
        self.file_out.close()

def extractFunctions(fcode):
    funcs = pythonast.parse(fcode)
    return funcs


if __name__ == '__main__':
    # path = 'test_input/CodeJam/2A/python/AdGold_A.py'
    path = 'core.py'
    pythonast = pythonast(path)
