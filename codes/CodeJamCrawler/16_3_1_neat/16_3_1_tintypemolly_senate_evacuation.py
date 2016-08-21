import string


def main():
    with open('A-large.in') as input_file, open('A-large.out', 'w') as output_file:
        case_count = int(input_file.readline().strip())
        for i in range(case_count):
            case_no = i + 1
            party_count = input_file.readline().strip()
            member_count_list = [int(m) for m in input_file.readline().strip().split(' ')]
            result = evacuate(party_count, member_count_list)
            output_file.write('Case #%s: %s\n' % (case_no, result))


class Party:
    def __init__(self, name, member_count):
        self.name = name
        self.member_count = member_count

    def __repr__(self):
        return '<Party %s, member_count: %d>' % (self.name, self.member_count)


def evacuate(party_count, member_count_list):
    all_member_count = sum(member_count_list)
    party_list = list()
    evac_order = list()
    for i, member_count in enumerate(member_count_list):
        party_list.append(Party(string.ascii_uppercase[i], member_count))

    party_list.sort(key=lambda p: p.member_count, reverse=True)

    while party_list:
        party_list.sort(key=lambda p: p.member_count, reverse=True)
        if len(party_list) > 2:
            if all_member_count > 3:
                if party_list[0].member_count - party_list[1].member_count < 2:
                    make_evac(party_list[0], party_list[1], evac_order)
                    all_member_count -= 2
                else:
                    make_evac(party_list[0], party_list[0], evac_order)
                    all_member_count -= 2
            else:
                make_evac_solo(party_list[0], evac_order)
                all_member_count -= 1
            party_list.sort(key=lambda p: p.member_count, reverse=True)
        else:
            make_evac(party_list[0], party_list[1], evac_order)
            all_member_count -= 2
        party_list = [p for p in party_list if p.member_count > 0]

    return ' '.join([''.join(e) for e in evac_order])


def make_evac_solo(party, evac_order):
    party.member_count -= 1
    evac_order.append(tuple(party.name))


def make_evac(party1, party2, evac_order):
    party1.member_count -= 1
    party2.member_count -= 1
    evac_order.append((party1.name, party2.name))


if __name__ == '__main__':
    main()
