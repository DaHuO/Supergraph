#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ast
import file_search
import sys
import re
import operator

class pythonast:
    def __init__(self, files_path, project_name):
        self.files_path = files_path
        self.IFSTRING = False
        self.file_out = open('test_results/HuffmanString_pythonast/'\
            + project_name + '_result.txt', 'w+')
        self.result = {}
        self.parse()
        self.finished()

    def parse(self):
        v = MyVisitor(self.IFSTRING)
        for f in self.files_path:
            if f[-3:] != '.py':
                pass
            else:
                ffile = open(f, 'r')
                fcode = ffile.read()
                print '#################' + f + '#################'
                expr_ast = ast.parse(fcode)
                dic = v.visit(expr_ast)
                dic_list = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
                self.file_out.write('#################' + f + '#################' + '\n')
                for dic in dic_list:
                    self.file_out.write(str(dic[0]) + '\t:\t' + str(dic[1]) + '\n')
                ffile.close()

    def finished(self):
        self.file_out.close()

class MyVisitor(ast.NodeVisitor):
    def __init__(self, IFSTRING):
        self.IFSTRING = IFSTRING
        self.result = {}

    def generic_visit(self, node):
        ast.NodeVisitor.generic_visit(self, node)
        return self.result

    def visit_Name(self, node):
        if node.id == '':
            return
        if node.id in self.result:
            self.result[node.id] += 1
        else:
            self.result[node.id] = 1

    def visit_Attribute(self, node):
        if node.attr == '':
            return
        if node.attr in self.result:
            self.result[node.attr] += 1
        else:
            self.result[node.attr] = 1

    def visit_Str(self, node):
        if not self.IFSTRING:
            return
        tokens = re.split('\||#|%|&|!|\(|\)|{|}|,|\.|\+|=|-|:|\\\|\/|' + \
            '\*|"|\'|;|\[|\]|<|>|\s*', node.s.strip())
        for token in tokens:
            if token == '':
                continue
            if token in self.result:
                self.result[token] += 1
            else:
                self.result[token] = 1

if __name__ == '__main__':
    input_arg = sys.argv
    path = 'test_codes/python/' + sys.argv[1]
    files_path = file_search.gci(path)
    pythonast = pythonast(files_path, sys.argv[1])
