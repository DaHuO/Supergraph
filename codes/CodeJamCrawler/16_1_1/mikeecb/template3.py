import bisect


num_test_cases = int(raw_input())


for test_case in range(num_test_cases):


    letters = raw_input()

    words = []


    for letter in letters: 

        if not words:
            words.append(letter)
            continue


    #    words = [word + letter for word in words] + [letter + word for word in words]

        new_words = []
        for word in words:
            if word[0] > letter:
                bisect.insort(new_words, word + letter)
            else:
                bisect.insort(new_words, letter + word)

        words = new_words

    result = words[len(words) - 1]

    #result = sorted(words)[len(words) - 1]       


    print "Case #" + str(test_case + 1) + ": " + result
