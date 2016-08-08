#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ast
import sys
import re
import operator

class pythonast:
    def __init__(self, file_path):
        # self.IFSTRING = False
        # self.file_out = open('astresult.txt', 'w')
        # self.result = {}
        self.parse(file_path)
        # self.finished()
        # self.count = 0

    def parse(self, file_path):
        # v = MyVisitor(self.IFSTRING)
        ffile = open(file_path, 'r')
        fcode = ffile.read()
        blocks = []
        print '#################' + file_path + '#################'
        try:
            expr_ast = ast.parse(fcode)
            self.dump(expr_ast.body, blocks, 0, True)
        except Exception, e:
            print Exception,":",e
        ffile.close()
        print blocks

    def dump(self, expr_list, blocks, parent, flag):
        if parent == 0:
            block = []
        else:
            block = [parent]
        for i in expr_list:
            if type(i).__name__ == 'FunctionDef':
                self.dump(i.body, blocks, i.lineno, True)
                continue
            if 'body' in i._fields:
                x = self.dump(i.body, blocks, i.lineno, False)
                block.extend(x)
            else:
                block.append(i.lineno)
        if flag:
            blocks.append(block)
        return block

    def finished(self):
        self.file_out.close()

class MyVisitor(ast.NodeVisitor):
    def __init__(self, IFSTRING):
        pass

    def visit_Name(self, node):
        if node.id == '':
            return
        if node.id in self.result:
            self.result[node.id] += 1
        else:
            self.result[node.id] = 1
        return node.id

    def visit_Attribute(self, node):
        if node.attr == '':
            return
        if node.attr in self.result:
            self.result[node.attr] += 1
        else:
            self.result[node.attr] = 1
        return node.attr

    def visit_FunctionDef(self, node):
        print(node.name)


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
        return node.str

if __name__ == '__main__':
    path = 'test_input/CodeJam/2A/python/AdGold_A.py'
    # path = 'core.py'
    pythonast = pythonast(path)
