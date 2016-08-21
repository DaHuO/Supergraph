# -*- coding: utf-8 -*-
def main():

    cases = int( input() )

    for case in range( cases ):

        target = [True] * 10

        number = int( input() )
        current = 0

        if number == 0:
            print( "Case #{}: INSOMNIA".format( case + 1 ) )

        else:
            while True in target:
                current += number
                for i in str( current ):
                    if target[int(i)]:
                        target[int(i)] = False
            print( "Case #{}: {}".format( case + 1, current ) )

        

if __name__ == "__main__":
    main()
