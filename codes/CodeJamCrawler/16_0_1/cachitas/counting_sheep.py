import logging


log = logging.getLogger(__name__)


def count_sheep(n):
    n = int(n)
    log.debug('INPUT N = %d' % n)
    asleep = False
    m = 1  # multiplier
    digits_seen = []
    iterations = 0  # counter; if it gets too large she will never fall asleep
    while not asleep:
        digits_seen = list(digits_seen)

        log.debug('Multiplier = %d' % m)
        named_number = n * m
        # see digits in named number
        log.debug('Named number = %s' % named_number)
        digits = [int(digit) for digit in str(named_number)]
        log.debug('Found %s in %d' % (digits, named_number))
        digits_seen.extend(digits)
        digits_seen = set(digits_seen)
        log.debug('Digits seen = %s' % digits_seen)

        iterations += 1

        if len(digits_seen) == 10:
            log.info('Fell asleep when reached %s' % named_number)
            return named_number
        elif iterations > 2000:
            log.info('Could not fall asleep after 2000 iterations')
            return 'INSOMNIA'
        else:
            log.debug('Still counting...')
            m += 1


if __name__ == '__main__':

    logging.basicConfig(level='DEBUG')

    T = int(input())  # read a line with a single integer (input size)
    for i in range(1, T + 1):
        N = input()
        print("Case #{}: {}".format(i, count_sheep(N)))
