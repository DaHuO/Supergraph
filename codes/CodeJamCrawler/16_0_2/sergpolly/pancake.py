import sys

# it's all about -(+-)n+ pattern:
# bottom +-ses are trimmed right away,
# (+-) - patterns are consumed, adding +2 to # of required flips, until EMPTY
# or until top-(-) pattern is encountered, which adds 1 to the flips numbers.
# THAT'S IT!!!!!!!!!!!!!!

def brave_get_flips(seq):
    num_flips = 0
    # bottom +ses do not affect anything at all ...
    seq = seq.rstrip('+')
    #
    while seq:
        # removing '+-' patterns or detecting top '-' ...
        score,seq = (2,seq.rstrip('-').rstrip('+')) if seq.rstrip('-') else (1,seq.rstrip('-')) 
        num_flips += score
    #
    return num_flips


problem_input = sys.stdin.readlines()
the_T = int(problem_input[0])
assert the_T == len(problem_input[1:])

for i,the_SEQ in enumerate(problem_input[1:]):
    print "Case #%d: %s"%(i+1,brave_get_flips(the_SEQ.strip()))














