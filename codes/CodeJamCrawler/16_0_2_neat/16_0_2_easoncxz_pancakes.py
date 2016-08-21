
flipped = {
    '-': '+',
    '+': '-'
    }

def flip_one(pancake):
    """
    >>> flip_one('-')
    '+'
    >>> flip_one('+')
    '-'
    """
    return flipped[pancake]

def flip_stack(stack: list, count: int) -> list:
    flipped = list(reversed(list(map(flip_one, stack[:count]))))
    kept = stack[count:]
    return flipped + kept

def flip_stack_str(stack_str: str, count: int) -> str:
    """
    >>> flip_stack_str('--+-', 4)
    '+-++'
    >>> flip_stack_str('--+-', 2)
    '+++-'
    """
    return ''.join(flip_stack(list(stack_str), count))

def find_first_index(char: str, stack: list) -> int:
    """
    >>> find_first_index('-', list('+++--'))
    3
    >>> find_first_index('-', list('---+++'))
    0
    >>> find_first_index('-', list('+++'))
    -1
    """
    def found(index):
        return stack[index] == char
    try:
        return next(filter(found, range(len(stack))))
    except StopIteration:
        return -1

def process_step(stack: list, begin_done: int) -> tuple:
    """
    >>> process_step(list('+++'), 0) == (list('+++'), 0)
    True
    >>> process_step(list('---+-++'), 5) == (list('+-+++++'), 2)
    True
    >>> process_step(list('+++----++'), 9) == (list('-------++'), 9)
    True
    """
    if begin_done == 0:
        return list(stack), 0
    elif stack[0] == '-':
        first_plus_index = find_first_index('+', stack)
        return flip_stack(stack, begin_done), (begin_done - first_plus_index)
    else:
        assert stack[0] == '+', repr(stack)
        first_minus_index = find_first_index('-', stack)
        return flip_stack(stack, first_minus_index), begin_done

def find_begin_done(stack_str: str) -> int:
    """
    >>> find_begin_done('----')
    4
    >>> find_begin_done('---++')
    3
    >>> find_begin_done('++++')
    0
    """
    last_minus_index = stack_str.rfind('-')
    return last_minus_index + 1    # Whether found '-' or not

def step_str(stack_str: str) -> str:
    """
    >>> step_str('--+-')
    '+-++'
    >>> step_str('---')
    '+++'
    >>> step_str('++---')
    '-----'
    >>> step_str('---++-')
    '+--+++'
    >>> step_str('---++-++')
    '+--+++++'
    """
    stack_before = list(stack_str)
    begin_done_before = find_begin_done(stack_str)
    stack_after, begin_done_after = process_step(stack_before, begin_done_before)
    return ''.join(stack_after)

def process(stack_str: str) -> iter:
    """
    >>> sum(1 for _ in process('+++'))
    0
    >>> sum(1 for _ in process('---'))
    1
    >>> sum(1 for _ in process('--+-'))
    3
    """
    before = stack_str
    while True:
        after = step_str(before)
        if after == before:
            return
        else:
            assert after != before, repr(after, before)
            yield after
            before = after

def run_process(stack_str: str) -> int:
    return sum(1 for _ in process(stack_str))

def main():
    count = int(input())
    for i in range(count):
        query = input()
        print("Case #{}: {}".format(i + 1, run_process(query)))

main()
