def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    open(output_filename, 'wb').close()
    with open(input_filename, 'r+b') as f:
        with open(output_filename, 'r+b') as g:
            T = int(f.readline().strip())
            for i in range(1, T+1):
                S = f.readline().strip()
                last_word = ''
                for s in S:
                    if last_word:
                        if s >= last_word[0]:
                            last_word = s + last_word
                        else:
                            last_word = last_word + s
                    else:
                        last_word = s
                print "Case #%d: %s" % (i, last_word)
                g.write("Case #%d: %s\n" % (i, last_word))

if __name__ == '__main__':
    main()