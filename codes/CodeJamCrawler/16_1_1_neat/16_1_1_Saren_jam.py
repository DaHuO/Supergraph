#!/usr/bin/env python3
from string import ascii_uppercase
FORMAT = "Case #{}: {}"

if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        s = input()
        win_word = s[0]
        for c in s[1:]:
            m_idx = ascii_uppercase.index(max(win_word, key=lambda x: ascii_uppercase.index(x)))
            idx = ascii_uppercase.index(c)
            if idx >= m_idx:
                win_word = c + win_word
            else:
                win_word += c
        print(FORMAT.format(case + 1, win_word))
