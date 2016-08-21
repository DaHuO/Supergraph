import sys
import re

def main ():

    prefix_pattern = re.compile (r"^(.+)0*$")
    default_answer = "INSOMNIA"
    T = int (sys.stdin.readline ().strip ())

    for t in range (T):

        N = int (sys.stdin.readline ().strip ())
        seen_digits = {}
        seen_prefixes = {}
        searching = True
        position = 1

        while searching:

            n = str (N * position)

            for character in n:

                seen_digits [character] = True
            
            if len (seen_digits.keys ()) == 10:

                searching = False
                answer = n

            else:

                prefix = prefix_pattern.sub (r"\1", n)

                if prefix in seen_prefixes.keys ():

                    searching = False
                    answer = default_answer

                else:

                    seen_prefixes [prefix] = True

            position += 1

        print ("Case #{}: {}".format (t + 1, answer))

    return 0

if __name__ == "__main__":

    exit (main ())
