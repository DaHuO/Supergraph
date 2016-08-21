import logging


log = logging.getLogger(__name__)

DIGITS = {          # unique occurences
    0: 'ZERO',      # Z
    1: 'ONE',       # O after 0s, 2s and 4s are removed
    2: 'TWO',       # W
    3: 'THREE',     # H after 8s are removed
    4: 'FOUR',      # U
    5: 'FIVE',      # F after 4s are removed
    6: 'SIX',       # X
    7: 'SEVEN',     # S after 6s are removed
    8: 'EIGHT',     # G
    9: 'NINE',      # I after 6s and 8s are removed
}


class PhoneNumber:

    def __init__(self, s):
        self.s = s
        self.sl = list(s)
        self.number = ''

        # Get the uniques first and remove associated letters
        self.remove_digit_with_unique_identifier(0, 'Z')
        self.remove_digit_with_unique_identifier(2, 'W')
        self.remove_digit_with_unique_identifier(4, 'U')
        self.remove_digit_with_unique_identifier(6, 'X')
        self.remove_digit_with_unique_identifier(8, 'G')

        self.remove_digit_with_unique_identifier(1, 'O')
        self.remove_digit_with_unique_identifier(3, 'H')
        self.remove_digit_with_unique_identifier(5, 'F')
        self.remove_digit_with_unique_identifier(7, 'S')
        self.remove_digit_with_unique_identifier(9, 'I')

        log.info("Phone number: %s", self.__str__())

    def __str__(self):
        return ''.join(sorted(self.number))

    def remove_digit_with_unique_identifier(self, digit, unique_id):
        occurences = self.s.count(unique_id)
        log.debug("Found %d %s in %s", occurences, DIGITS[digit], self.s)

        # Remove digit letters
        for c in DIGITS[digit]:
            self.s = self.s.replace(c, '', occurences)

        # Add digit
        self.number += occurences * str(digit)


if __name__ == '__main__':

    logging.basicConfig(
        level='INFO',
        format='[%(levelname)-8s] %(name)s: %(message)s'
    )

    T = int(input())  # read a line with a single integer (input size)
    for i in range(1, T + 1):
        log.info(50 * '-' + ' CASE {:>d}'.format(i))
        S = [s for s in input().split(" ")]
        log.info('Input: S={}'.format(S))

        for s in S:
            print("Case #{}: {}".format(i, PhoneNumber(s)))
