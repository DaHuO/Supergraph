#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# standard module
import os
import sys

# install required

# from local script

class Codejam2Solver:

    def __init__(self, initial_state):
        self.cakes = initial_state

    def get_answer(self):
        stack_separated_by_happy = self.cakes.split("+")
        is_needed_reverse_cakes_first_time = "-" in stack_separated_by_happy[0]

        if len(stack_separated_by_happy) > 1:
            step_needed = len([section for section in stack_separated_by_happy[1:] if "-" in section]) * 2
        else:
            step_needed = 0

        if is_needed_reverse_cakes_first_time:
            step_needed += 1

        return step_needed

lines = [line.strip() for line in open(sys.argv[1])]
target = lines[1:int(lines[0])+1]
for i, cakes in enumerate(target):
    print(cakes)
    solver = Codejam2Solver(cakes)
    print("Case #{0}: {1}".format(i + 1 , solver.get_answer()))
