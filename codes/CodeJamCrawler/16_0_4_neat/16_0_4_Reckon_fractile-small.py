n_cases = int(raw_input())



for i in range(0, n_cases):
    line = raw_input().split()
    K = int(line[0])
    C = int(line[1])
    S = int(line[2])

    # This will print out numbers 1 to K for the solution.
    # This is always correct when S = K.
    # The reason is as follows:
    #
    # For any pattern, the first letter of the pattern is the first letter of any sequence of
    # any complexity C.
    # Therefore, if G is the first letter of the original pattern, G is the first letter of all
    # sequences of any complexity.
    # This means that for the first letter of complexity C-1 is the same as the one for
    # complexity C.
    # If the first letter of the sequence in complexity C-1 was G, then the first K letters
    # of complexity C are G by construction.
    # If the first letter of the sequence in complexity C-1 was L, then the first K letters
    # of complexity C are the original K letter sequence.
    #
    # As long as S = K, then we can use all the graduate students to discover the original
    # sequence. All but one of the 2^K possible original patterns have a G. The last one is
    # all L. Therefore, no complexity will ever have a G since L cannot introduce a G.
    ans = map(str, range(1, K+1))

    s = ' '.join(ans)
    
    print "Case #" + str(i+1) + ":", s
