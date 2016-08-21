def change(inputstring):
    if inputstring=='+':
        return '-'
    else:
        return '+'
def flip(all_cakes,num_to_flip):
    flippers = all_cakes[:num_to_flip]
    flipped_flippers = [change(cake) for cake in flippers[::-1]]
    all_cakes[:num_to_flip] = flipped_flippers
    return all_cakes

def pancake(pancake_string):
    cakes=list(pancake_string)
    # print ''.join(cakes)
    num_flips=0
    while True:
        if all([cake=='+' for cake in cakes]):
#             print "Done! That took %i flips"%num_flips
            return num_flips
        if all([cake=='-' for cake in cakes]):
            flip(cakes,len(cakes))
            num_flips+=1
#             print "Done! That took %i flips"%num_flips
            return num_flips

        if cakes[0]=='-':
            #This finds the index of the first + pancake in the stack        
            first_good_cake_index = next(i for i in range(len(cakes)) if cakes[i]=='+')

            #Flip to this point
            flip(cakes,first_good_cake_index)
            # print ''.join(cakes)
            num_flips+=1

        if all([cake=='+' for cake in cakes]):
            return num_flips
            break
      
        
        first_bad_cake_index = next(i for i in range(len(cakes)) if cakes[i]=='-')
        flip(cakes,first_bad_cake_index)
        num_flips+=1

        # print ''.join(cakes)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    cakestring=raw_input()
    # print num
    result = pancake(cakestring)
    print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options