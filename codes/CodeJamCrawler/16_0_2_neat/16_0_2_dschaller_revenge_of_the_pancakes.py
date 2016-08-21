class RevengeOfThePankcakes(object):
    def __init__(self):
        self.number_of_flips = 0

    def analyze_stack(self, stack):
        last_downside_index = None
        index = 1
        for pancake in stack:
            if pancake == '-':
                last_downside_index = index
            index += 1

        if last_downside_index is None:
            return self.number_of_flips

        self.number_of_flips += 1
        flipping_stack = stack[0:last_downside_index]
        flipping_stack = flipping_stack.replace('+', 't')
        flipping_stack = flipping_stack.replace('-', '+')
        flipping_stack = flipping_stack.replace('t', '-')
        return self.analyze_stack(
            '{}{}'.format(flipping_stack, stack[last_downside_index+1:])
        )


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = str(raw_input())
        result = RevengeOfThePankcakes().analyze_stack(n)
        print "Case #{}: {}".format(i, result)
