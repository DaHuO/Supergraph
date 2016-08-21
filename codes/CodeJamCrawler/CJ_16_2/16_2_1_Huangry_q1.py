def remove(dc_letters, word, n_times):
    for letter in word:
        dc_letters[letter] -= n_times

with open('A-large.in', 'r') as f:
    with open('q1solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            S = f.readline()
            letters = dict()
            answer = ""
            for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                letters[letter] = 0
            for letter in S:
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1
            if 'X' in letters:
                n = letters['X']
                answer += '6'*n
                remove(letters, 'SIX', n)
            if 'Z' in letters:
                n = letters['Z']
                answer += '0'*n
                remove(letters, 'ZERO', n)
            if 'W' in letters:
                n = letters['W']
                answer += '2'*n
                remove(letters, 'TWO', n)
            if 'G' in letters:
                n = letters['G']
                answer += '8'*n
                remove(letters, 'EIGHT', n)
            if 'T' in letters:
                n = letters['T']
                answer += '3'*n
                remove(letters, 'THREE', n)
            if 'R' in letters:
                n = letters['R']
                answer += '4'*n
                remove(letters, 'FOUR', n)
            if 'F' in letters:
                n = letters['F']
                answer += '5'*n
                remove(letters, 'FIVE', n)
            if 'V' in letters:
                n = letters['V']
                answer += '7'*n
                remove(letters, 'SEVEN', n)
            if 'N' in letters:
                n = letters['I']
                answer += '9'*n
                remove(letters, 'NINE', n)
            if 'O' in letters:
                n = letters['O']
                answer += '1'*n
                remove(letters, 'ONE', n)

            answer_sorted = ''.join(sorted(answer))

            solution.write('Case #' + str(case+1) + ': ' + answer_sorted + '\n')

        solution.closed
    f.closed