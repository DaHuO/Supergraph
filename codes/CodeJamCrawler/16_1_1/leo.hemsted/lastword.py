from collections import deque, namedtuple
WordThing = namedtuple('WordThing', ['word', 'next_chars'])

def get_last_word(s):
    word_queue = deque()
    word_queue.append(WordThing(word='', next_chars=s))
    lastwords = set()
    while len(word_queue):
        thing = word_queue.popleft()
        if thing.next_chars:
            word_queue.append(WordThing(word=thing.word + thing.next_chars[0], next_chars=thing.next_chars[1:]))
            word_queue.append(WordThing(word=thing.next_chars[0] + thing.word, next_chars=thing.next_chars[1:]))
        else:
            lastwords.add(thing.word)
    return sorted(lastwords)[-1]



test_cases = int(input())

for test_case in range(1, test_cases + 1):
    output_word = get_last_word(input())
    print('Case #{}: {}'.format(test_case, output_word))
