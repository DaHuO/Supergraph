from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

with open('B-large.in', 'r') as input_file, open('B.out', 'w') as output_file:
    tc = int(input_file.readline())
    for cc in range(tc):
        cleaned_string = reduce(
            lambda x, y: x + y if y != x[-1] else x,
            input_file.readline(),
        )
        result, _  = reduce(
            lambda x, y: (
                min(x[0] + 2 * int(y=='-'), x[1] + 1),
                min(x[0] + 1, x[1] + 2 * int(y=='+'))
            ),
            cleaned_string,
            (0, 0),
        )
        output_file.write('Case #{}: {}\n'.format(cc+1, result))
