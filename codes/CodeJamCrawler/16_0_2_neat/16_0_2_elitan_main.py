#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    for i in range(int(input())):
        pc = input() # pancakes!
        if not '-' in pc:
            print('Case #%d: 0' % (i+1))
            continue
        
        # remove trailing happy cakes
        while pc[-1] == '+':
            pc = pc[:-1]

        # just count how many times the cakes have to switch
        current_mood = pc[0]
        c = 1
        for mood in pc:
            if mood != current_mood:
                current_mood = mood
                c += 1
        print('Case #%d: %d' % (i+1, c))


if __name__ == "__main__":
    main()
