import os
import click


@click.argument('out_file', type=click.File('w'))
@click.argument('in_file', type=click.File('r'))
@click.command()
def main(in_file, out_file):
    cases = [int(x) for x in in_file][1:]
    for i, c in enumerate(cases, 1):
        sol = solve(c)
        out_file.write("Case #{}: {}\n".format(i, solve(c)))

def solve(c):
    if c == 0:
        return "INSOMNIA"
    i = 1
    k = [0 for _ in range(10)]
    while not all(k):
        for d in str(c*i):
            k[int(d)] = 1
        i+=1

    return c * (i-1)


if __name__ == '__main__':
    main()
