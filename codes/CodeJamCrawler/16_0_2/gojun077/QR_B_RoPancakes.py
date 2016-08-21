# This program requires Python 3

# Google Code Jam 2016 Qualification Round Problem B
# Revenge of the Pancakes
# https://code.google.com/codejam/contest/6254486/dashboard#s=p1

# Problem:

#  The Infinite House of Pancakes has just introduced a new kind of
#  pancake! It has a happy face made of chocolate chips on one side
#  (the "happy side"), and nothing on the other side (the "blank
#  side").

# You are the head waiter on duty, and the kitchen has just given you
# a stack of pancakes to serve to a customer. Like any good pancake
# server, you have X-ray pancake vision, and you can see whether each
# pancake in the stack has the happy side up or the blank side up. You
# think the customer will be happiest if every pancake is happy side
# up when you serve them.

# You know the following maneuver: carefully lift up some number of
# pancakes (possibly all of them) from the top of the stack, flip that
# entire group over, and then put the group back down on top of any
# pancakes that you did not lift up.

# When flipping a group of pancakes, you flip the ENTIRE group in one
# motion; you do not individually flip each pancake.

# Formally: if we number the pancakes 1, 2, ..., N from top to bottom,
# you choose the top i pancakes to flip. Then, after the flip, the
# stack is i, i-1, ..., 2, 1, i+1, i+2, ..., N.

# Example I choose the top 3 pancakes to flip out of 4 total
# |[1]|
# |[2]|
# |[3]|
# [4]

# After flipping the group of 3 pancakes, the stack will look like:
# [3]
# [2]
# [1]
# [4]

# Pancakes 1, 2, 3 would now have the opposite side showing from
# before, while pancake 4 would still have the same side showing

# For example, let's denote the happy side as + and the blank side as
# -. Suppose that the stack, starting from the top, is:

# --+-
# You could flip the top 3 pancakes to make
# -++-
# Flip the top pancake to make
# +++-
# and then flip the top 3 to make
# ----
# Finally flip the whole stack to make
# ++++ (4 flips)


# You will not serve the customer until every pancake is happy side
# up, but you don't want the pancakes to get cold, so you have to act
# fast! What is the smallest number of times you will need to execute
# the maneuver to get all the pancakes happy side up, if you make
# optimal choices?

# INPUT
# The first line of the input gives the number of test cases, T. T
# test cases follow. Each consists of one line with a string S, each
# character of which is either + (which represents a pancake that is
# initially happy side up) or - (which represents a pancake that is
# initially blank side up). The string, when read left to right,
# represents the stack when viewed from top to bottom.

# LIMITS

# 1 <= T <= 100.
# Every character in S is either + or -.

# Small dataset
# 1 <= length of S <= 10.

# Large dataset
# 1 <= length of S <= 100.


INFILE = "B-large.in"
OUTFILE = "B-large.out"


def load_file(infile):
    '''
    String -> Listof ListOfString
    Take a GCJ newline and space-delimited textfile and process it
    so that the entire file is a list with each line as a sublist
    made up of individual words

    'all your base\n' -> ['all', 'your', 'base']
    '''
    inputL = []
    with open(infile, 'r') as f:
        for line in f:
            line.replace('\n', '')
            # Split words on whitespace and insert in list
            inputL.append(line.split())
    return inputL


def num_cases(list_file):
    '''
    ListOfString -> Int

    Pop the first element from list_file and convert it to int

    **NOTE**: this function mutates the input list!

    >>> num_cases(['5', '--+-'])
    5
    '''
    ncases = int(list_file.pop(0)[0])
    return ncases


def next_case(list_file):
    '''
    ListOfString -> String
    Given a list of strings, return the next string element
    of the form '+-++' which represents a stack of pancakes S
    with each pancake s_i having a sign of either '+' meaning
    'smiley side up' or '-' meaning 'bare side up'

    **NOTE**: this function mutates the input list!

    >>> next_case([['-+-'], ['+-+'], ['++++']])
    '-+-'

    >>> next_case([])
    []
    '''
    if list_file == []:
        return []
    else:
        return list_file.pop(0)[0]


def makePancakeL(pancakes):
    '''
    String -> ListOfInt
    Given a string of the form '+-+--' containing only pluses and
    minuses, return a List of Ints converting '+' to 1 and '-' to -1

    >>> makePancakeL('+')
    [1]

    >>> makePancakeL('+-+')
    [1, -1, 1]

    >>> makePancakeL('+-++')
    [1, -1, 1, 1]
    '''
    pancakeL = []
    for i in range(len(pancakes)):
        if pancakes[i] == '+':
            pancakeL.append(1)
        elif pancakes[i] == '-':
            pancakeL.append(-1)
    return pancakeL


def all_happy(listp):
    '''
    List -> Boolean
    Given a list of integer 1's and -1's return true if all
    list elements are 1; return False otw

    >>> all_happy([1, -1, 1])
    False

    >>> all_happy([1, 1, 1, 1, 1])
    True

    >>> all_happy([1, 1, 1, 1, -1])
    False
    '''
    happy_flag = True

    for i in listp:
        if i != 1:
            happy_flag = False
            return happy_flag
    return happy_flag


def all_minus(listp):
    '''
    List -> Boolean
    Given a list of integer 1's and -1's return true if all
    list elements are -1; return False otw

    >>> all_minus([1, -1, 1])
    False

    >>> all_minus([-1, -1, -1, -1, -1])
    True

    >>> all_happy([-1, -1, -1, -1, 1])
    False
    '''
    minus_flag = True

    for i in listp:
        if i != -1:
            minus_flag = False
            return minus_flag
    return minus_flag


def flipSign(num):
    '''
    Int -> Int
    Flip the sign of the integer passed in as input

    >>> flipSign(1)
    -1

    >>> flipSign(-1)
    1
    '''
    return num * -1


def flipRange(listp):
    '''
    ListOfInt -> ListOfInt

    Change the sign of an entire list

    >>> flipRange([1, 1])
    [-1, -1]

    >>> flipRange([-1])
    [1]

    >>> flipRange([-1, -1, 1])
    [1, 1, -1]
    '''
    new_listp = []
    for i in listp:
        new_listp.append(flipSign(i))
    return new_listp


def flipPancakes(listp):
    '''
    ListOfInt -> Int

    Given a List of Ints 1 or -1, this function will return the number
    of flips required to make the entire list consist of only 1's
    Note that all flip ranges must at least include the top pancake.

    >>> flipPancakes([-1])
    1

    >>> flipPancakes([1])
    0

    >>> flipPancakes([1, 1])
    0

    >>> flipPancakes([-1, 1])
    1

    >>> flipPancakes([1, -1])
    2

    >>> flipPancakes([-1, -1, -1, -1])
    1

    >>> flipPancakes([-1, -1, 1, -1])
    3

    >>> flipPancakes([1, 1, -1])
    2

    >>> flipPancakes([1, -1, 1])
    2

    >>> flipPancakes([1, -1, 1, 1])
    2

    >>> flipPancakes([1, -1, 1, -1])
    4

    >>> flipPancakes([1, 1, 1, -1])
    2

    >>> flipPancakes([1, 1, 1, 1, -1])
    2
    '''
    copy_listp = listp
    fcount = 0 # number of flips
    index_cnt = 0
    index_limit = len(listp) - 1

    while not all_happy(copy_listp):
        if all_minus(copy_listp):
            return fcount + 1
        elif index_cnt == index_limit:
            return fcount + 1
        # if L[i] != L[i+1], flip L[0:i+1]
        elif copy_listp[index_cnt] != copy_listp[index_cnt + 1]:
            # change sign of all elements in list before (index_cnt + 1)
            frontL = []
            frontL.extend(flipRange(copy_listp[:index_cnt + 1]))

            # define the remainder part of the original listp
            backL = copy_listp[index_cnt + 1:]

            # update listp by combining frontL and backL
            frontL.extend(backL)
            copy_listp = frontL

            fcount += 1

        # if none of the other conditions holds, increment the index
        # counter and go on to next iteration of loop
        # i.e. If L[i] == L[i+1], increment counter and then check
        # if L[i+1] == L[i+2]
        index_cnt += 1

    return fcount


def write_out(outfile):
    '''
    Write result to output file by calling helper functions
    load_file(), num_cases() next_case(), makePancakeL() and the
    logic function flipPancakes():
    1. load_file() strips newlines and adds strings to a list,
       splitting on whitespace
    2. num_cases() gets the number of cases from the list created by
       load_file()
    3. next_case() returns the next case of the form '+--+'
       which needs to be parsed into ListOfInt
    4. makePancakeL() converts a string into a ListOfInt and passes
       the loi to flipPancakes()
    5. flipPancakes analyzes the pancake stack and returns the no. of
       flips req'd to make all happy sides face up
    '''
    with open(outfile, 'w') as outf:
        input_list = load_file(INFILE)
        copy_input = input_list
        case_cnt = 1

        for i in range(num_cases(copy_input)):
            ans = flipPancakes(makePancakeL(next_case(copy_input)))
            outf.write('Case #' + str(case_cnt) + ': ' + str(ans) + '\n')
            case_cnt += 1


# MAIN PROGRAM
import doctest
doctest.testmod()
write_out(OUTFILE)
