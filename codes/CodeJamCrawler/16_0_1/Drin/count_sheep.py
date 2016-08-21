import os
import sys

import itertools

class SheepCounter(object):
    previous_sheep_counts = {}

    @classmethod
    def is_asleep(cls): return len(digits_seen) is 10

    @classmethod
    def count_sheep(cls, initial_num):
        if initial_num in cls.previous_sheep_counts:
            return cls.previous_sheep_counts[initial_num]

        digits_seen = set()
        last_num = None

        count_generator = (
            multiplier * initial_num
            for multiplier in itertools.count(1)
        )

        while len(digits_seen) is not 10:
            next_num = next(count_generator)
            if last_num is not None and next_num == last_num:
                cls.previous_sheep_counts[initial_num] = 'INSOMNIA'
                return 'INSOMNIA'

            digits_seen |= set([digit for digit in str(next_num)])
            last_num = next_num

        if last_num is None:
            cls.previous_sheep_counts[initial_num] = 'INSOMNIA'
            return 'INSOMNIA'

        cls.previous_sheep_counts[initial_num] = last_num
        return last_num

if __name__ == '__main__':
    num_inputs = None
    num_iter = 0
    for line in sys.stdin:
        if num_inputs is None:
            num_inputs = int(line.strip())

        elif num_iter < num_inputs:
            print('Case #{0}: {1}'.format(
                num_iter + 1,
                SheepCounter.count_sheep(int(line.strip()))
            ))

            num_iter += 1

        else:
            sys.exit('Found more inputs than specified')
    '''
    print(SheepCounter.count_sheep(0))
    print(SheepCounter.count_sheep(1))
    print(SheepCounter.count_sheep(2))
    print(SheepCounter.count_sheep(11))
    print(SheepCounter.count_sheep(1692))
    '''
