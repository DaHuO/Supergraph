#!/usr/bin/python

t = int(raw_input())
for i in xrange(1, t + 1):
    words = list(raw_input())
    board = [ words.pop(0) ]
    while len(words) > 0:
        word = words.pop(0)
        if ord(board[0]) > ord(word):
            board.append(word)
        else:
            board.insert(0, word)
    print "Case #{}: {}".format(i, ''.join(board))