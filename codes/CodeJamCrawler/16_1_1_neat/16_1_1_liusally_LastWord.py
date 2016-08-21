

def main():
    of = open('lastword-large.out', 'w', 1)

    with open('A-large.in', 'r') as f:
        count = int(f.readline().rstrip('\n'))
        for i in range(count):
            line = f.readline().rstrip('\n')
            string = line

            output = ''
            for ch in string:
                if len(output) == 0:
                    output += ch
                else:
                    if ch >= output[0]:
                        output = ch + output
                    else:
                        output += ch

            of.write('Case #{}: {}\n'.format(i + 1, output))


    of.close()

if __name__ == "__main__":
    main()
