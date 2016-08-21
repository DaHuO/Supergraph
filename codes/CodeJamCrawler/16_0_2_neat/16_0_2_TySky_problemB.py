# -*- coding: utf-8 -*-
def main():

    cases = int( input() )

    for case in range( cases ):

        pancakes = list( input() )
        result   = 0

        for i in range( 1, len( pancakes ) ):

            if pancakes[i] != pancakes[i - 1]:
                result += 1

        if pancakes[-1] == "-":
            result += 1

        print( "Case #{}: {}".format( case + 1, result ) )

        

if __name__ == "__main__":
    main()
