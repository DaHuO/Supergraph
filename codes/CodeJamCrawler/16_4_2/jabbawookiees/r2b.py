cases = int(raw_input())

for ctr in xrange(cases):
    n, k = [int(x) for x in raw_input().split(" ")]
    probs = [float(x) for x in raw_input().split(" ")]
    probs.sort()

    best_prob = 0.0
    for left in xrange(k + 1):
        left_list = probs[:left]
        right = k - left
        if right != 0:
            right_list = probs[-right:]
        else:
            right_list = []
        # print left_list, right_list

        current_probabilities = {
            0: 1.0
        }
        chosen = left_list + right_list
        for prob in chosen:
            next_probabilities = {}
            for key, value in current_probabilities.items():
                next_probabilities[key + 1] = value * prob
            # print "Mext", next_probabilities
            for key, value in current_probabilities.items():
                if next_probabilities.get(key) is None:
                    next_probabilities[key] = 0.0
                next_probabilities[key] += current_probabilities[key] * (1 - prob)
            # print "Mexter", next_probabilities

            current_probabilities = next_probabilities
            # print current_probabilities
        best_prob = max(best_prob, current_probabilities[k / 2])
    print "Case #%d: %f" % (ctr + 1, best_prob)
