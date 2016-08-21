import click

def flip(stack, top):
    for i in range(0, top+1):
        stack[i] = '-' if stack[i] == '+' else '+'


def solve(stack):
    last = len(stack) - 1
    moves = 0

    while not all([x == '+' for x in stack]):
        for i in range(last, -1, -1):
            if stack[i] == '+':
                continue
            flip(stack, i)
            moves += 1
            last = i-1
            break

    return moves


@click.command()
@click.argument('in_file', type=click.File('r'))
@click.argument('out_file', type=click.File('w'))
def main(in_file, out_file):
    cases = [list(x.strip()) for x in in_file][1:]
    for i, c in enumerate(cases, 1):
        out_file.write("Case #{}: {}\n".format(i, solve(c)))
    

if __name__ == '__main__':
    main()
