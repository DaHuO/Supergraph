from string import ascii_lowercase

def main():
    nums = {
        'eight': 8,
        'zero': 0,
        'four': 4,
        'three': 3,
        'two': 2,
        'six': 6,
        'one': 1,
        'seven': 7,
        'nine': 9,
        'five': 5,
    }
    for t in range(1, 1 + int(input())):
        s = input().lower()
        counts = {x: 0 for x in ascii_lowercase}
        for x in s:
            counts[x] += 1
        phno = []
        for ch, num in (('g', 'eight'), ('z', 'zero'), ('u', 'four'), ('h', 'three'), ('t', 'two'), ('x', 'six'), ('o', 'one'), ('s', 'seven'), ('n', 'nine'), ('v', 'five')):
            while counts[ch]:
                for x in num:
                    counts[x] -= 1
                phno.append(nums[num])
        # while counts['g']:
        #     for x in 'eight':
        #         counts[x] -= 1
        # while counts['z']:
        #     for x in 'zero':
        #         counts[x] -= 1
        # while counts['u']:
        #     for x in 'four':
        #         counts[x] -= 1
        # while counts['h']:
        #     for x in 'three':
        #         counts[x] -= 1
        # while counts['t']:
        #     for x in 'two':
        #         counts[x] -= 1
        # while counts['x']:
        #     for x in 'six':
        #         counts[x] -= 1
        # while counts['o']:
        #     for x in 'one':
        #         counts[x] -= 1
        # while counts['s']:
        #     for x in 'seven':
        #         counts[x] -= 1
        # while counts['n']:
        #     for x in 'nine':
        #         counts[x] -= 1
        # while counts['v']:
        #     for x in 'five':
        #         counts[x] -= 1


        print('Case #%d: %s' % (t, ''.join(map(str, sorted(phno)))))

main()
