#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def flip(row, n):
    temp = row[:n]
    for i in range(n):
        if temp[i] == '+':
            row[n-i-1] = '-'
        else:
            row[n-i-1] = '+'
    return row


def check(row):
    count = 0
    for x in row:
        if x == '+':
            count += 1
    if count == len(row):
        return True
    else:
        return False


def compute(row):
    len_row = len(row)
    count = 0
    for i in range(len_row-1):
        if row[i] != row[i+1]:
            row = flip(row, i)
            count += 1
            if check(row):
                return count
    if row[-1] == '-':
        row = flip(row, len(row))
        count += 1
    return count


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        cases = f.readline()
        for i in range(int(cases)):
            row = [item for item in f.readline().strip()]
            result = compute(row)
            print('Case #{}: {}'.format(i+1, result))
