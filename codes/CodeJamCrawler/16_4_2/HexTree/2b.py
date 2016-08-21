import itertools

with open("data.txt", 'r') as f:
    with open("data1.txt", 'w') as g:
        T = int(f.readline())
        for i in range(T):
            N, K = [int(x) for x in f.readline().split()]
            P = [int(x.replace('.', '')) for x in f.readline().split()]
            P.sort()

            yesmen = P[-(K/2):]
            nomen = P[:K/2]

            candidates = [nomen + yesmen]

            best1 = None
            bestscore = K*100 + 1
            targetscore = K*50

            for selection in itertools.combinations(P, K):
                score = sum(selection)
                if abs(score-targetscore) < abs(bestscore-targetscore):
                    best1 = selection
                    bestscore = score

            best1 = list(best1)
            candidates.append(best1)

            limit = 8000
            for selection in itertools.combinations(P, K):
                candidates.append(list(selection))
                if len(candidates) >= limit:
                    break

            print i+1
            best = 0.00

            for cand in candidates:
                result = 0.00
                for yesmen in itertools.combinations(cand, K/2):
                    no = cand[:]
                    yes = []
                    for x in yesmen:
                        yes.append(x)
                        no.remove(x)

                    prob = 1.00
                    for x in yes:
                        prob *= (x / 100.0)
                    for x in no:
                        prob *= ((100 - x) / 100.0)
                    result += prob

                best = max(best, result)

            # best = None
            # bestscore = K*100 + 1
            # targetscore = K*50
            #
            # for selection in itertools.combinations(P, K):
            #     score = sum(selection)
            #     if abs(score-targetscore) < abs(bestscore-targetscore):
            #         best = selection
            #         bestscore = score
            #
            # best = list(best)
            # print P, best
            #
            # result = 0.00
            #
            # for yesmen in itertools.combinations(best, K/2):
            #     no = best[:]
            #     yes = []
            #     for x in yesmen:
            #         yes.append(x)
            #         no.remove(x)
            #
            #     prob = 1.00
            #     for x in yes:
            #         prob *= (x / 100.0)
            #     for x in no:
            #         prob *= ((100 - x) / 100.0)
            #     result += prob
            #
            #     print i+1, yes, no, prob
            # print best, prob

            g.write("Case #%d: %f\n" % ((i + 1), best))