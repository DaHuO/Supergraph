###############################################################################
#      Coded by Hai Brenner (Israel) for the Google Code Jam Competition      #
###############################################################################

from functools import wraps, update_wrapper
import time
import os

###############################
#      useful decorators
###############################

__memoization_registry = []
_CALL_FUNC_COUNTERS = {}


# a decorator for memoizing function outputs
def memoize_it(inner_func):
    global __memoization_registry
    cache = {}
    __memoization_registry.append(cache)

    @wraps(inner_func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = inner_func(*args, **kwargs)
        return cache[args]
    return wrapper


# clear all previous memoization. For use in the beginning of a new test-case
def reset_memoization():
    global __memoization_registry
    try:
        for cache_d in __memoization_registry:
            cache_d.clear()
    except NameError:
        pass


# a decorator to add time benchmarking for a function
def time_it(inner_func):
    @wraps(inner_func)
    def wrapper(*args, **kwargs):
        print('--> Start function \'' + inner_func.__qualname__ + '\' : ', time.ctime())
        start_time = time.time()
        res = inner_func(*args, **kwargs)
        end_time = time.time()
        print('--> End   function \'' + inner_func.__qualname__ + '\' : ', time.ctime())
        print('--> Elapsed time \'' + inner_func.__qualname__ + '\' : ', end_time-start_time)
        print()
        return res
    return wrapper


# a decorator for logging the function's inputs and outputs
def log_it(arguments=True, output=True):
    def decorating_function(user_function):
        def wrapper(*args, **kwargs):
            if arguments:
                print(time.ctime(),
                      ': function \'' + user_function.__qualname__ + '\' arguments args=', args, 'kwargs=', kwargs)
            result = user_function(*args, **kwargs)
            if output:
                print(time.ctime(), ': function \'' + user_function.__qualname__ + '\' outputs ', result)
            return result
        return update_wrapper(wrapper, user_function)
    return decorating_function

        
# a decorator for counting the number of calls to the wrapped function
def count_it(inner_func):
    global _CALL_FUNC_COUNTERS
    assert type(_CALL_FUNC_COUNTERS) == dict
    assert inner_func.__qualname__ not in _CALL_FUNC_COUNTERS
    _CALL_FUNC_COUNTERS[inner_func.__qualname__] = 0

    @wraps(inner_func)
    def wrapper(*args, **kwargs):
        global _CALL_FUNC_COUNTERS
        _CALL_FUNC_COUNTERS[inner_func.__qualname__] += 1
        return inner_func(*args, **kwargs)
    return wrapper


# a decorator for pre-processing the function and automatically save the result
def pre_process_it(inner_func):
    import inspect
    import pickle
    a = inspect.signature(inner_func)
    if len(a.aparmeters):
        raise ValueError('A pre process function must not have arguments')
    
    @time_it
    @wraps(inner_func)
    def wrapper(*args, **kwargs):
        filename = 'pre-process_' + inner_func.__qualname__ + '.pickle'
        if filename not in os.listdir():
            print('--> Pre process started for function \'' + inner_func.__qualname__ + '\' ....')
            pre_process_data = inner_func()
            print('--> Pre process ended for function \'' + inner_func.__qualname__ + '\'')
            print('--> Pickling started for function \'' + inner_func.__qualname__ + '\' ....')
            with open(filename, 'wb') as f_pp:
                pickle.dump(pre_process_data, f_pp, pickle.HIGHEST_PROTOCOL)
            print('--> Pickling ended for function \'' + inner_func.__qualname__ + '\'')
        print('--> Unpickling pre-processed data of function \'' + inner_func.__qualname__ + '\' ...')
        with open(filename, 'rb') as f_pp:
            data = pickle.load(f_pp)
        print('--> Unpickling ended')
        print()
        return data

    return wrapper
 

###########################################
# automatic runner
###########################################

# a class to wrap automatically the IO files in one class
class GCJIOWrapper:

    def __init__(self, input_filename, parsed_filename, output_filename):
        self.__input_filename = input_filename
        self.__parsed_filename = parsed_filename
        self.__output_filename = output_filename
        self.__index_test_case = 0
        self.__input_file = None
        self.__parsed_file = None
        self.__output_file = None

    def __enter__(self):
        # open the IO files
        self.__input_file = open(self.__input_filename, 'r')
        self.__parsed_file = open(self.__parsed_filename, 'w')
        self.__output_file = open(self.__output_filename, 'w')

    def __exit__(self, type_e, value, tb):
        # close the IO files
        self.__input_file.close()
        self.__parsed_file.close()
        self.__output_file.close()

    def readline(self):
        # read one line from the input. write it as is to the parsed file
        l = self.__input_file.readline()
        self.__parsed_file.write(l)
        return l
    
    def new_test_case(self):
        # mark a new test case to the parsed file
        self.__index_test_case += 1
        self.__parsed_file.write('\n## _BigOnion Test case: ' + str(self.__index_test_case) + ' ##\n')
    
    def write(self, s):
        # write to the output file
        self.__output_file.write(s)
    
    def get_test_case(self):
        # return the index of the current test case
        return self.__index_test_case
        

# This is the automatic runner    
@time_it
def main_run():
        
    # find the most current input file (.in) which is in the working directory 
    print('Directory : ', os.getcwd())
    file_names = [x for x in os.listdir()]
    l1 = [(os.stat(x).st_mtime, x) for x in file_names if x.endswith('.in')]
    if not l1:
        raise ValueError('No input file found')
    chosen_prefix = sorted(l1)[-1][1][:-3]
    input_filename = chosen_prefix + '.in'
    print('Chosen Input : ', input_filename)
    
    # filename of the file into which to parse the input file
    parsed_filename = chosen_prefix + '.parsed.txt'

    # filename of the output file. It has the same prefix, 
    # and it doesn't tread over the previous output file from previous attempts
    l2 = [x.split('.')[0] for x in file_names if x.endswith('.out') and x.startswith(chosen_prefix)]
    l2 = [int(x.split('-run')[-1]) for x in l2]
    output_file_index = ('000' + str(max([0] + l2) + 1))[-3:]
    output_filename = chosen_prefix + '-run' + output_file_index + '.out'
    print('Chosen Output : ', output_filename)
    print()
    
    io_wrapper = GCJIOWrapper(input_filename, parsed_filename, output_filename)
    with io_wrapper:
        solve_all_cases(io_wrapper)

    # print the chosen files once again for easy checking of correctness
    print()
    print('Conclusion :')
    print('Directory : ', os.getcwd())
    print('Chosen Input : ', input_filename)
    print('Chosen Output : ', output_filename)


# the automatic solver. Handles the test case mechanism
@time_it
def solve_all_cases(io_wrapper):
    T = int(io_wrapper.readline())
    for test_case in range(1, T+1):
        io_wrapper.new_test_case()
        assert io_wrapper.get_test_case() == test_case
        solve_one_case(io_wrapper)


###########################################
# write code here
###########################################

ROCK = 'R'
PAPER = 'P'
SCISSORS = 'S'

def solve_one_case(io_wrapper):
    # fill details here
    N, R, P, S = [int(x) for x in io_wrapper.readline().split()]
    assert R+P+S == 2**N
    solution = find_solution(N, R, P, S)
    io_wrapper.write('Case #' + str(io_wrapper.get_test_case()) + ': ' + solution + '\n')


def find_solution (N, R, P, S):
    a = try_winner(ROCK, N, R, P, S)
    print(a)
    if a is not None:
        a = alphabetically_first_solution(a)
    else:
        a = 'Z'
    b = try_winner(PAPER, N, R, P, S)
    print(b)
    if b is not None:
        b = alphabetically_first_solution(b)
    else:
        b = 'Z'
    c = try_winner(SCISSORS, N, R, P, S)
    print(c)
    if c is not None:
        c = alphabetically_first_solution(c)
    else:
        c = 'Z'
    print()
    if a == b == c == 'Z':
        return 'IMPOSSIBLE'
    return min(a, b, c)


def try_winner(winner, N, R, P, S):
    l = [winner]
    for _round in range(N):
        l2 = []
        for i in l:
            if i == ROCK:
                l2.extend([ROCK, SCISSORS])
            elif i == PAPER:
                l2.extend([PAPER, ROCK])
            else:
                assert i == SCISSORS
                l2.extend([SCISSORS, PAPER])
        l = l2
    if l.count(ROCK) == R and l.count(PAPER) == P and l.count(SCISSORS) == S:
        return l
    return None


def alphabetically_first_solution(l):
    jump = 1
    while jump < len(l):
        for s in range(0, len(l), 2*jump):
            t1 = l[s:s+jump]
            t2 = l[s+jump:s+2*jump]
            if t2 < t1:
                l[s+jump:s+2*jump] = t1
                l[s:s+jump] = t2
        jump *= 2
    assert jump == len(l)
    return ''.join(l)



main_run()
