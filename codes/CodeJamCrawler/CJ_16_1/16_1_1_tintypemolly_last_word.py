def main():
    with open('A-large.in') as input_file, open('A-large.out', 'w') as output_file:
        case_count = int(input_file.readline().strip())
        for i in range(case_count):
            case_no = i + 1
            input_word = input_file.readline().strip()
            last_word = list()
            for word in input_word:
                if all((word >= c for c in last_word)):
                    last_word.insert(0, word)
                else:
                    last_word.append(word)
            output_file.write('Case #%d: %s\n' % (case_no, ''.join(last_word)))


if __name__ == '__main__':
    main()