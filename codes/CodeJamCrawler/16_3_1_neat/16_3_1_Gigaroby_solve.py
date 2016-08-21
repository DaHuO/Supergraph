import click
from string import ascii_uppercase as al

def is_majority(case):
    tot = sum(case)
    for n in case:
        if n > tot/2:
            return n
    return -1

def pick_party(pn, parties):
    fp = parties[0]
    sp = parties[1]
    pn[fp] -= 1
    if pn[fp] < pn[sp]:
        parties.sort(key=lambda i: pn[i], reverse=True)

    return fp


def solve(case):
    out = []
    n, pn = case
    parties = list(range(n))
    parties.sort(key=lambda i: pn[i], reverse=True)
    while not all(x == 0 for x in pn):
        p = pick_party(pn, parties)
        if is_majority(pn) != -1:
            pp = pick_party(pn, parties)
            out.append((p, pp))
        else:
            out.append((p,))

        k = is_majority(pn)
        if k != -1:
            print(k, pn)


    return " ".join([''.join(al[i] for i in t) for t in out])

def read_numbers(f):
    return [int(x) for x in f.readline()]

def cases(f):
    one = True
    n = 0
    for line in f:
        if one:
            n = int(line.strip())
        else:
            senators = [int(x) for x in line.strip().split()]
            yield n, senators
        one = not one

@click.command()
@click.argument('in_file', type=click.File('r'))
@click.argument('out_file', type=click.File('w'))
def main(in_file, out_file):
    in_file.readline()
    for i, case in enumerate(cases(in_file), 1):
        out_file.write("Case #{}: {}\n".format(i, solve(case)))

if __name__ == '__main__':
    main()


