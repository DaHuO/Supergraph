#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tokenize
import file_search
import sys
import re
import operator

class pythontokenize:
    def __init__(self, files_path, project_name):
        self.IFCOMMENT = True
        self.files_path = files_path
        self.file_out = open('test_results/HuffmanString_pythontokenize/'\
            + project_name + '_result.txt', 'w+')
        self.result = {}
        self.parse()
        self.finished()

    def parse(self):
        for f in self.files_path:
            if f[-3:] != '.py':
                pass
            else:
                ffile = open(f, 'r')
                print '########## ' + f + ' ##########'
                dic = {}
                def handle_token(type, token, (srow, scol), (erow, ecol), line):
                    # print "%d,%d-%d,%d:\t%s\t%s" % \
                    # (srow, scol, erow, ecol, tokenize.tok_name[type], repr(token))
                    if tokenize.tok_name[type] == 'NAME':
                        token = str(token).strip()
                        if not token:
                            return
                        if token in dic:
                            dic[token] += 1
                        else:
                            dic[token] = 1
                        return
                    if tokenize.tok_name[type] == 'STRING':
                        tokens = str(token)
                        tokens_list = re.split('\||#|%|&|!|\(|\)|{|}|,|\.|\+|=|-|:|\\\|\/|' + \
                            '\*|"|\'|;|\[|\]|<|>|\s*', tokens)
                        for token in tokens_list:
                            token = token.strip()
                            if not token:
                                return
                            if token in dic:
                                dic[token] += 1
                            else:
                                dic[token] = 1
                        return
                    if self.IFCOMMENT and tokenize.tok_name[type] == 'COMMENT':
                        tokens = str(token)
                        tokens_list = re.split('\||#|%|&|!|\(|\)|{|}|,|\.|\+|=|-|:|\\\|\/|' + \
                            '\*|"|\'|;|\[|\]|<|>|\s*', tokens)
                        for token in tokens_list:
                            token = token.strip()
                            if not token:
                                return
                            if token in dic:
                                dic[token] += 1
                            else:
                                dic[token] = 1
                        return

                tokenize.tokenize(ffile.readline, handle_token)
                dic_list = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
                self.file_out.write('############# ' + f + ' #############' + '\n')
                for dic in dic_list:
                    self.file_out.write(str(dic[0]) + '\t:\t' + str(dic[1]) + '\n')
                ffile.close()
                

    def finished(self):
        self.file_out.close()


if __name__ == '__main__':
    input_arg = sys.argv
    path = 'test_codes/python/' + sys.argv[1]
    files_path = file_search.gci(path)
    pythontokenize = pythontokenize(files_path, sys.argv[1])
