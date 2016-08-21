
# Original sequence GLLL: GGGG GLLL GLLL GLLL
# Original sequence LGLL: LGLL GGGG LGLL LGLL
# Original sequence LLGL: LLGL LLGL GGGG LLGL
# Original sequence LLLG: LLLG LLLG LLLG GGGG
#                          X           X
#                            X    X


#Notice, Nothing with at least 1 G can have LL at 2,12
#Nothing with 1 G can have L at 4 and 8

# Hypothesis 1: Each 'Check' actually checks two possible blocks,

# Checking any number from 1-K when C >= 2:
# We can do this WLOG for any complexity larger than 2, because the first
# (K^2) values (K Blocks of size K) remain constant for all larger complexities.
#

# This rules out the starting sequence GLL, because the first K letters would
# be all Gold.

# Therefore, it makes no sense to check 1, instead by checking anything from
# i in 2-K, for any value of i:
# You also rule out the formation L*(i - 1) + G + L*(k - i) as the starting one.

# Therefore, in some arrangement, it makes sense to check in order:
# The 2nd in block 1 (2), the 4th in block 3 (K*2 + 4), the 6th in block 5 (K*4 + 6), etc.
# This may be out of range, when K is odd..
# If K is odd however, we can just check any number in the Kth block, so just iterate the last loop
# one less time, and use the last one to check the very last Letter in the first K^2 block

# This also means the minimum number of checks is ceiling of (K/2)
# When C >= 2, or the all values K when C = 1.


import math
q_num = input()

for q in range(int(q_num)):

    inputs = input().split()
    K = int(inputs[0])
    Complex = int(inputs[1])
    Students = int(inputs[2])
    result = ""
    ## Original Edge Case K == 1
    if K == Students:
        for i in range(K):
            result = result + " "+ str(i+1)
    ## When Complexity is 1
    elif Complex == 1:

        if Students < K:
            result = " IMPOSSIBLE"

        elif Students >= K:
            for i in range(K):
                result = result + " " + str(i+1)

    ## You always have at least K/C Checks!
    elif Complex > 1:
        numberofchecks = math.ceil(K/Complex)
        if Students < numberofchecks:
            result = " IMPOSSIBLE"

        elif K%Complex == 0:
            for i in range(numberofchecks):
                check_index = 0
                starting_check = Complex * i


                ## The checked index is some sorta power series I dont even know
                ## We are checking for G at the spot K * i + 1 spot till the K*i + C + 1 spot
                for j in range(Complex):
                    block_check = starting_check + j
                    size = K**(Complex-j-1)
                    check_index += (size*block_check)

                result = result + " " + str(check_index + 1)


        elif K%Complex >= 1:
            for i in range(numberofchecks):
                check_index = 0
                starting_check = Complex * i
                right = K - starting_check
                if right > Complex:
                    for j in range(Complex):
                        block_check = starting_check + j
                        size = K**(Complex-j-1)
                        check_index += (size*block_check)
                else:
                    for j in range(right):
                        block_check = starting_check + j
                        size = K**(Complex-j-1)
                        check_index += (size*block_check)

                result = result + " " + str(check_index + 1)






    print("Case #" + str(q+1) + ":" + str(result))

## Can larger Complexites cause more patterns?

#  LGLGGGLGL    GGGGGGGGG   LGLGGGLGL
#  LLGLLGGGG    LLGLLGGGG   GGGGGGGGG
#  GGGGGGGGG    GGGGLLGLL   GGGGLLGLL

# Ok, so 0 + 6, 9 + 3, 9 + 7, or 18 + 2, 18 + 4 all end up being single checks that work.

# Take these values as block 9 blocks of three,
# By taking the 3rd value from the second block, we remove possibilities
# 1 - because it is all part of the huge first block (1-9)
# 2 - because it is part of the second block (4-6)
# 3 - Because it is the third of the second block (6)

# Now lets take blocks of size 5 with complexity three:
# Rule out 1 by taking a number from (1-25)
# Rule out 2 by taking a number from (6-10)
# Rule out 3 by takiing the third number in that block (8)

# Rule out 4 by taking a number from (76-100)
# Rule out 5 by taking a numer from (96-100)

# Now lets take blocks of size 6 with complexity three (total of 6^3 = 216):
# Rule out 1 by taking a number from (1-36)
# Rule out 2 by taking a number from (7-12)
# Rule out 3 by takiing the third number in that block (9) = 0 * 36 + 1 * 6  + 2 * 1

# Rule out 4 by taking a number from (109-145)
# Rule out 5 by taking a numer from (134-138)
# Rule out 6 by taking a the 6th number in that block (138) = 3 * 36 + 4 * 6 + 5 * 1

# So we have the summation of C terms.
## Image the number Block = 1 for the first one and Block = 4 for the second (Corresponding to
## Values of K/C), in our case where we have blocks of size 6 with complexity 3
## (Block -1) * K^C + (Block) * K^{C-1} + (Block+1) * K^{C-2}
## result_i = \Simga_k=0^{2} (Block - k -1 ) * K^{C-k}

## The number of results are therefore ceil K/C which is the sum of C items

## 7 with complexity 4: 1 2 3 4         5 6 7


# Now lets take blocks of size 4 with complexity 4 (total of 4^4 = 256):
# Rule out 1 by taking a number from (1-64)
# Rule out 2 by taking a number from (17 - 32)
# Rule out 3 by takiing  a num from (25-28)
