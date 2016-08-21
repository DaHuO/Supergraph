import sys
from collections import deque

def checkHappy(configuration):
    isHappy = True
    for i in configuration:
        if i != '+':
            isHappy = False
            break
    return isHappy

with open(sys.argv[1]) as f:
    content = f.read().splitlines()

with open('io/pancakes.out', 'w') as f:
    T = int(content[0])
    for caseIndex in xrange(1, T+1):
        configuration = content[caseIndex]

        # implementing BFS
        # the queue contains tuples of pancake configuration and moves thus far
        queue = deque([(configuration, 0)])
        # keep track of configuration already explored (so we don't do it repeatedly)
        exploredConfigurations = {configuration: True}
        while len(queue):
            oldConfiguration, steps = queue.popleft()
            
            # debug
            # print 'Interediate #%d: %s, steps: %d' % (caseIndex, oldConfiguration, steps)

            if checkHappy(oldConfiguration):
                f.write('Case #%d: %d\n' % (caseIndex, steps))
                print 'Case #%d: %d' % (caseIndex, steps)
                break

            for i in range(len(oldConfiguration)):
                # make new configuration by flipping top i+1 pancakes
                newConfigurationList = list(oldConfiguration)
                for j in range(i+1):
                    newConfigurationList[j] = '-' if oldConfiguration[i - j] == '+' else '+'
                newConfiguration = ''; 
                for j in newConfigurationList:
                    newConfiguration += j;
                
                if newConfiguration not in exploredConfigurations:
                    queue.append((newConfiguration, steps + 1))
                    exploredConfigurations[newConfiguration] = True