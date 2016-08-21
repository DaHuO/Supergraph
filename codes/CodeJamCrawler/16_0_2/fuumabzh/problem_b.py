class Waiter:
    def __init__(self, input_name):
        self.input_name = input_name
        self.stacks = list()
        self.res = list()
        self.input()
        for i, stack in enumerate(self.stacks):
            print(i)
            self.res.append(self.solve(stack))
        self.output()

    def input(self):
        with open(self.input_name, 'r') as f:
            for i, l in enumerate(f):
                l = l.split('\n')[0]
                if i > 0:
                    self.stacks.append([e == '+' for e in l][::-1])

    def output(self):
        output_name = 'output_' + self.input_name
        with open(output_name, 'w') as f:
            for i, r in enumerate(self.res):
                printline = 'Case #' + str(i + 1) + ': {0} \n'.format(str(r))
                print(printline)
                f.write(printline)

    def reverse_stack(self, stack, idx):
        return [not e for e in stack[idx:]][::-1]

    def test_symmetrical_case(self, stack):
        return not(stack[0]) == stack[-1] or stack == self.reverse_stack(stack, 0)

    def solve(self, stack):
        # method able to do recursive call
        check_pancake = 0
        maneuver_number = 0
        stack_size = len(stack)
        while check_pancake < stack_size:
            #print(stack)
            if not stack[0]:
                #  If the top stack - 1 is only True things, they fast solving
                if sum(stack[1:]) == len(stack) - 1 and len(stack) > 1:
                    #print('fast')
                    maneuver_number += 2
                    check_pancake = stack_size
                # If the top stack is the symmetrical (just like in case 3)
                elif self.test_symmetrical_case(stack):
                    #print('sym')
                    # We are forced to solve the inverse problem and then just do a final flip
                    maneuver_number += 1 + self.solve([not e for e in stack[1:]])
                    check_pancake = stack_size
                else:
                    #print('class')
                    cmp = 0
                    while cmp < len(stack) and not stack[-cmp-1]:
                        cmp += 1
                    stack = self.reverse_stack(stack, 0)[cmp:]
                    maneuver_number += 1
                    check_pancake += cmp
            else:
                #print('advance')
                check_pancake += 1
                stack = stack[1:]
        return maneuver_number


if __name__ == '__main__':
    # w = Waiter('input_test.txt')
    # w = Waiter('B-small-attempt4.in')
    W = Waiter('B-large.in')
