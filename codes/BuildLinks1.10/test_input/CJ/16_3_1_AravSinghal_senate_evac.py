from math import ceil
from typing import List, Dict, Tuple

from redef_io import input, print_file, get_delimited_int_list

t = int(input())


def half(sen: List[int]):
    return int(ceil((sum(sen) + 1) / 2))


def build_cache(sen: List[int]) -> Dict[int, List[int]]:
    cache = {}  # type: Dict[int, List[int]]

    for i, s in enumerate(sen):
        cache[s] = cache.get(s, []) + [i]

    return cache


def remove(items: List[int], sen: List[int]) -> str:
    op = ''
    remove_count = min(2, len(items) - 2)
    remove_count = 2 if remove_count == 0 else remove_count

    for i, item in enumerate(items):
        if i == remove_count:
            break
        sen[item] -= 1
        op += chr(65 + item)

    assert 0 < len(op) <= 2
    return op


def evac(sen: List[int]) -> str:
    op = ''

    cache = build_cache(sen)
    m = max(cache.keys())

    while m != 0:
        op += remove(cache[m], sen) + ' '

        cache = build_cache(sen)
        m = max(cache.keys())

    return op


for it in range(t):
    n = int(input())

    sen = get_delimited_int_list()

    output = evac(sen)
    print_file(output.strip())
