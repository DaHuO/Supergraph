# -*- coding: utf-8 -*-
import fileinput
import itertools

def run():

    in_stream = fileinput.input()
    cases_count = int(in_stream.readline())

    for case in xrange(cases_count):
        start_number = int(in_stream.readline())
        multiplier = 1
        numbers_left = set(xrange(10))
        no_changes_iterations = 0
        while no_changes_iterations < 100:
            len_before = len(numbers_left)
            digits = set(itertools.imap(int, str(start_number * multiplier)))
            numbers_left -= digits
            if len_before == len(numbers_left):
                no_changes_iterations += 1
            if not numbers_left:
                print("Case #{0}: {1}".format(case+1, start_number * multiplier))
                break
            multiplier += 1
        else:
            print("Case #{0}: INSOMNIA".format(case+1))

if __name__ == "__main__":
    run()
