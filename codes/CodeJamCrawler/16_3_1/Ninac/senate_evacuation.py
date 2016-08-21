def main():
    file = open('A-large.in', 'rU')
    lines = iter(file.readlines())
    file.close()

    case_count = int(next(lines))

    for case_idx in range(1, case_count + 1):
        party_count = int(next(lines))

        parties = [int(x) for x in next(lines).split()]
        names = [x for x in range(65, 65 + party_count)]
        politician_count = sum(parties)
        case_output = []

        parties = [[x, y] for x, y in zip(parties, names)]

        while politician_count > 0:
            parties = sorted(parties)
            parties[-1][0] -= 1
            politician_count -= 1
            step = chr(parties[-1][1])
            if parties[-1][0] == 0:
                parties.pop(-1)

            if len(parties) == 2 and parties[0][0] == parties[1][0] and parties[0][0] < 4:
                case_output.append(step)
                continue

            parties = sorted(parties)
            parties[-1][0] -= 1
            politician_count -= 1
            step += chr(parties[-1][1])

            if parties[-1][0] == 0:
                parties.pop(-1)

            case_output.append(step)

        print('Case #{}: {}'.format(case_idx, ' '.join(case_output)))


if __name__ == '__main__':
    main()
