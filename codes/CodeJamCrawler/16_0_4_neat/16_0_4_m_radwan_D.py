from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import functools

with open('D-large.in') as f, open('D2.out', 'w') as output:
    tc = int(f.readline())
    for cc in range(tc):
        k, c, s = map(int, f.readline().split())
        needed = map(
            lambda x: str(reduce(lambda a, b:a*k + b, x) + 1),
            [[x for x in range(a, min(a + c, k))] for a in range(0, k, c)]
        )
        output.write("Case #{}: {}\n".format(
            cc+1,
            ' '.join(needed) if len(needed) <= s else "IMPOSSIBLE"
        ))
