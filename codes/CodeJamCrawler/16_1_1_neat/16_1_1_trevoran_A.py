with open('A-large.in', 'r') as file_in, open('A-large.out', 'w') as file_out:
    lines = file_in.readlines()

    t = int(lines[0])
    for case in range(1, t + 1):
        s = lines[case].strip()
        last_word = [s[0]]
        for char in s[1:]:
            if char >= last_word[0]:
                last_word.insert(0, char)
            else:
                last_word.append(char)
        file_out.write('Case #{}: {}\n'.format(case, ''.join(last_word)))