from collections import defaultdict

def observe(observation, number):
    x = number
    while x > 0:
        observation[x%10] += 1
        x /= 10

def is_sleep(observation):
    if len(observation.keys()) == 10:
        return True
    return False

cases = input()

for c in range(cases):
    observation = defaultdict(int)
    N = input()
    if N == 0:
        print "Case #{0}: INSOMNIA".format(c+1)
        continue
    i = 1
    while not is_sleep(observation):
        n = N * i
        observe(observation, n)
        i += 1
    print "Case #{0}: {1}".format(c+1, n)

