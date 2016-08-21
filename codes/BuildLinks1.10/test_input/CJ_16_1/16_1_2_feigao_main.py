#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
from functools import wraps, lru_cache


def io_wrapper(func):
    @wraps(func)
    def _func(in_file=None, out_file=None, lines_per_case=1):
        in_buffers = []
        if in_file is None:
            while True:
                try:
                    s = input()
                    if s.strip():
                        in_buffers.append(s.strip())
                except:
                    break
        else:
            with open(in_file, 'r') as f:
                in_buffers.extend([line.strip() for line in f.read().strip().splitlines()])
        total_case_nums = int(in_buffers[0])
        in_buffers = in_buffers[1:]
        assert len(in_buffers) == total_case_nums * lines_per_case

        out_buffers = []
        for case_id in range(1, total_case_nums + 1):
            case_result_str = func('\n'.join(in_buffers[(case_id - 1) * lines_per_case: case_id * lines_per_case]))
            out_buffers.append('Case #{}: {}'.format(case_id, case_result_str))

        if out_file is not None and os.path.exists(out_file):
            print('Out file {} already exists!'.format(out_file), file=sys.stderr)
            out_buffers = None
        if out_file is None:
            print('\n'.join(out_buffers))
        else:
            with open(out_file, 'w') as f:
                f.write('\n'.join(out_buffers))

    return _func


@io_wrapper
@lru_cache(maxsize=None)
def solution(line_str):
    return "Answer Str"


@io_wrapper
@lru_cache(maxsize=None)
def the_last_word(line_str):
    prefix, suffix = '', ''
    for i in range(len(line_str) - 1, -1, -1):
        if line_str[i] >= max(line_str[:i + 1]):
            prefix = prefix + line_str[i]
        else:
            suffix = line_str[i] + suffix
    return prefix + suffix


def B_wrapper(in_file, out_file=None):
    def rank_and_file(N, lsts):
        from collections import Counter
        from functools import reduce
        from operator import add
        nums = Counter(reduce(add, lsts, []))
        result = []
        for n, c in nums.items():
            if c % 2 == 1:
                result.append(n)
        result.sort()
        assert len(result) == N
        return result

    in_lines = open(in_file).read().strip().splitlines()[::-1]
    case_nums = int(in_lines.pop())
    out_buffers = []

    for case_id in range(1, case_nums + 1):
        N = int(in_lines.pop())
        lsts = []
        for j in range(2 * N - 1):
            lsts.append(list(map(int, in_lines.pop().split())))
        result = rank_and_file(N, lsts)
        out_buffers.append(' '.join(map(str, result)))

    if out_file is None:
        f = sys.stdout
    else:
        f = open(out_file, 'w')
    for i, line in enumerate(out_buffers, 1):
        f.write('Case #{}: {}\n'.format(i, line))


@io_wrapper
# @lru_cache(maxsize=None)
def bffs(lines_str):
    n_str, b_str = lines_str.splitlines()
    n = int(n_str)
    bffs = [int(s) - 1 for s in b_str.split()]
    best = 0

    ends = [-1] * n
    visit = [set() for _ in range(n)]

    for i in range(n):
        j = i
        while j not in visit[i]:
            visit[i].add(j)
            ends[i] = j
            j = bffs[j]
        if bffs[ends[i]] == i and len(visit[i]) > best:
            best = len(visit[i])
    for i in range(n):
        ei = ends[i]
        for j in range(i + 1, n):
            ej = ends[j]
            if visit[i].intersection(visit[j]) == {ei, ej} and bffs[ei] == ej and bffs[ej] == ei:
                best = max(best, len(visit[i] | visit[j]))
    return str(best)


if __name__ == '__main__':
    # the_last_word('A-sample.txt', lines_per_case=1)
    # the_last_word('A-large.in.txt', 'A-large.out.txt')

    # B_wrapper('B-sample.txt')
    # B_wrapper('B-small-attempt0.in.txt', 'B-small-attempt0.out.txt')
    B_wrapper('B-large.in.txt', 'B-large.out.txt')

    # bffs('C-sample.txt', lines_per_case=2)
    # bffs('C-small-attempt0.in.txt', lines_per_case=2)
