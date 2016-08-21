#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 2.7
# @Author: Moming

def get_tile_index(k, c, s):
    """
    if k == s and k != 1:
        result = [x for x in range(2, k + 1)]
        return result
    elif k == s and k == 1:
        return [1]
    else:
        return []
    """
    result = [x for x in range(1, k +1)]
    return result

# main
if __name__ == '__main__':
    fr = open('./D-small-attempt2.in', 'r')
    fw = open('./result.in', 'w')
    T = int(fr.readline())

    i = 0
    result = []
    while i < T:
        i += 1
        temp = fr.readline().split(' ')
        (K, C, S) = (int(x) for x in temp)
        result = get_tile_index(K, C, S)
        fw.write('Case #%d:' % i)
        if len(result) == 0:
            fw.write(' IMPOSSIBLE\n')
        else:
            for index in result:
                fw.write(' %d' % index)
            fw.write('\n')

    fr.close()
    fw.close()
