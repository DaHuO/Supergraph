
#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 2.7
# @Author: Moming

def last_word(cmd):
    result = cmd[0]
    for i in range(len(cmd))[1 : ]:
        if cmd[i] >= result[0]:
            result = cmd[i] + result
        else:
            result = result + cmd[i]

    return result



# main
if __name__ == '__main__':
    fr = open('./A-large.in', 'r')
    fw = open('./result.in', 'w')
    T = int(fr.readline())

    for i in range(T):
        cmd = fr.readline()
        fw.write('Case #%d:' % (i + 1))
        cmd = last_word(cmd)
        fw.write(' %s' % cmd)
