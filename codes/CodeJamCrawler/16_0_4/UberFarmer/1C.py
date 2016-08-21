from sys import stdin

DEBUG = False

def debug_print(*args):
    if DEBUG:
        print args

def main():
    num_cases = int(stdin.readline())
    for case in range(1, num_cases + 1):
        line = stdin.readline().strip().split()
        K = int(line[0])
        C = int(line[1])
        S = int(line[2])

        divisor = K / C
        remainder = K % C
        if remainder:
            num_to_check = divisor + 1
        else:
            num_to_check = divisor

        if S < num_to_check:
            print "Case #{}: IMPOSSIBLE".format(case)
            continue

        debug_print("K", K, "C", C, "S", S, "num_to_check", num_to_check)
        debug_print("remainder", remainder)
        debug_print(locals())
        orig_positions_to_confirm = range(K)
        if remainder:
            for i in range(C - remainder):
                orig_positions_to_confirm.append(orig_positions_to_confirm[-1])
        debug_print(orig_positions_to_confirm)
        assert len(orig_positions_to_confirm) == C * num_to_check

        spots_to_check = []

        while orig_positions_to_confirm:
            final_spot_to_check = 0
            for level in range(C):
                final_spot_to_check *= K
                orig_position_to_confirm = orig_positions_to_confirm.pop(0)
                final_spot_to_check += orig_position_to_confirm
                debug_print(final_spot_to_check, orig_position_to_confirm)

            final_spot_to_check += 1

            spots_to_check.append(final_spot_to_check)

        output_spots = ""
        for spot in spots_to_check:
            output_spots += " " + str(spot)
        print "Case #{}:{}".format(case, output_spots)

if __name__ == "__main__":
    main()
