def rabbits(n):
    if n==0:
        return "INSOMNIA"
    seen = []
    m=n
    while len(seen) < 10:
        for i in str(n):
            if not i in seen:
                seen.append(i)
        n += m
    n-= m
    return n
cases = """0
1
2
11
1692
452652
7
80139
847767
574462
168724
389414
721974
607658
966241
581843
8
533417
999993
999998
125679
999994
125
3
496143
555357
469078
966861
643928
958757
405734
566914
284835
628144
305501
999995
641502
40
468007
4
6
474102
999991
8420
999992
706958
412291
12500
829738
989530
1000000
999999
124
649921
934380
524408
452026
47241
566779
48575
545212
166
176944
685651
995445
660536
910087
427902
336090
882662
528479
125000
434055
749191
461737
270659
155418
26704
883168
200
362135
513729
747709
87897
392284
999996
57048
20
25
999997
5
147414
195867
34
1250
695602
9
10
87817
632395""".split()
for i in xrange(len(cases)):
    print "Case #%d: %s" %(i+1, rabbits(int(cases[i])))
        