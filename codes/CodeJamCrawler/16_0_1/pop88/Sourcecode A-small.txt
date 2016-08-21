def seen_digits(inpt):
    case = 0
    for line in inpt:
        if not case:
            case += 1
            continue
        elif line == '\n':
            continue
        else:
            number = int(line[:-1])
            if not number:
                print('Case #' + str(case) + ': INSOMNIA\n')
                case += 1
            else:
                seen = ()
                copy, incre = number, number
                while len(seen) < 10:
                    for digit in str(copy):
                        if int(digit) not in seen:
                            seen += (int(digit),)
                    copy += incre
                print('Case #' + str(case) + ': ' + str(copy - incre) + '\n')
                case += 1
