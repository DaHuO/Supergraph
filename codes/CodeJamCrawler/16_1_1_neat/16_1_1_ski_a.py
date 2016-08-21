import sys
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
info = log.info
dbg = log.debug


def solve(case):
    variants = [case[0]]


    for l in case[1:]:
        variants = [(v+l) for v in variants] + [(l+v) for v in variants]

    return max(variants)


def solve2(case):
    """
    >>> cases = ['BSMFHSAOSH',
    ... 'CFTPXIECTZQU',
    ... 'YUOZVOBLOIL',
    ... 'YQERUNTABQ',
    ... 'GCRDHSQWN',
    ... 'TGUKZFTE',
    ... 'OYAINOEV',
    ... 'ZURXIOZW',
    ... 'LBYWFLEP',
    ... 'EXQHJXNP',
    ... 'PCKESLJV',
    ... 'TGXYBAFT',
    ... 'UXKHZAXR',
    ... 'ELPRNXFX',
    ... 'IRRVDVYC',
    ... 'SIZPDZPL',
    ... 'WSBUWACX',
    ... 'SKFXPGTH',
    ... 'HBTUISUW',
    ... 'ICGVPSGR']
    >>> all(solve(c) == solve2(c) for c in cases)
    True
    """
    out = [case[0]]
    for l in case[1:]:
        if l >= out[0]:
            out.insert(0, l)
        else:
            out.append(l)
    return ''.join(out)


def get_cases(lines):
    for ln in lines[1:]:
        yield ln.strip()


def main():
    lines = [ln.strip() for ln in sys.stdin]

    for i, case in enumerate(get_cases(lines), 1):
        log.info('Solving #%d: %r', i, case)
        #r = solve(case)
        r2 = solve2(case)
        #assert r == r2, (r, r2)
        print 'Case #%d: %s' % (i, r2)


if __name__ == '__main__':
    main()
