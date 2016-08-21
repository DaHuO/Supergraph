#!/usr/bin/python

# from set import Set

def allUp(number):
    if '-' in list(number) :
        return False
    return True



def counting(number, steps, states):
    if len(number) > 0 and number not in states:
        states.append(number)
        if allUp(number):
            # print 'Found' + str(steps)
            return steps
        else:
            stepss = []
            for i in range(1, len(number)):

                nk = flip(number[:i]) + number[(i):]
                # print '-->> ' + nk + ' ' + str(steps+1)
                if allUp(nk):
                    # print 'Found' + str(steps+1)
                    stepss.append(steps+1)
                else:

                    cnt = counting(nk, steps + 1, list(states))
                    if cnt != None:
                        stepss.append(cnt)


            if len(stepss) > 0:
                # print 'Found' + str(min(stepss))
                return min(stepss)


def endPila(pila):
    for i in pila:
        if i['found'] == False:
            return True
    return False

def notInStateStep(state, states):
    sss = [ss for ss in states if ss['num'] == state['num'] and ss['step'] > state['step']]
    if len(sss) > 0:
        return False
    return True

def plusAtTheEnd(s):
    s = list(s)
    s.reverse()
    cnt = 0
    for i in s:
        if i == '+':
            cnt += 1
        else:
            return cnt
    return cnt

def negativesBeginning(s):
    s = list(s)
    s.reverse()
    cnt = 0
    for i in s:
        if i == '-':
            cnt += 1
        else:
            return cnt
    return cnt

import random

def countingNoPila(number):
    number = number.replace('\n','')
    stack = []
    stack.append({
        'number': number,
        'found': False,
        'steps': 0
    })
    states = []
    shortest = 10000000000
    while endPila(stack):
        # print stack
        stack = [ss for ss in stack if ss['steps'] <= shortest]
        state = stack.pop()
        # print str(state) +  ' not in '
        # print states
        stateToComapre = {
            'num': state['number'],
            'step': state['steps']
        }
        if notInStateStep(stateToComapre, states) and state['steps'] < shortest:
            states.append({
                'num': state['number'],
                'step': state['steps']
            })
            # print 'states = ' + str(states)
            if state['found'] == False:
                # print 'state not found'
                if allUp(state['number']):
                    # print 'Found2'
                    state['found'] = True
                    stack.insert(0,state)
                    if state['steps'] < shortest:

                        shortest = state['steps']

                else:

                    # nn=negativesBeginning(state['number'])
                    # if nn > 1:
                    #     nk = flip(state['number'][:nn]) + state['number'][nn:]
                    #     if allUp(nk):
                    #         print 'Found ' + str(state['steps'] + 1)
                    #         print state['number']
                    #         print nk
                    #         print '------'
                    #         stack.insert(0,{
                    #             'number': nk,
                    #             'found': True,
                    #             'steps': state['steps'] + 1
                    #         })
                    #         if state['steps'] < shortest:
                    #             shortest = state['steps'] + 1
                    #             # print 'new short ' + str(shortest)
                    #     else:
                    #         stateToComapre = {
                    #             'num': nk,
                    #             'step': state['steps'] + 1
                    #         }
                    #         if notInStateStep(stateToComapre, states):
                    #             # states.append(nk)
                    #             stack.append({
                    #                 'number': nk,
                    #                 'found': False,
                    #                 'steps': state['steps'] + 1
                    #             })
                    # else:

                    # print 'fucking in'
                    # for i in reversed(range(1, len(state['number']) + 1)):
                    # pp = plusAtTheEnd(state['number'])
                    # if (len(state['number']) + 1 - pp) > 1:
                        # print str(len(state['number']) + 1 - pp)
                        # nums = [x for x in range(1, len(state['number']) + 1 - pp)]
                    nums = [x for x in range(1, len(state['number']) + 1)]
                    random.shuffle(nums)
                    for i in nums:

                        nk = flip(state['number'][:i]) + state['number'][i:]
                        # print 'new nk = ' + nk
                        if allUp(nk):
                            # print 'Found ' + str(state['steps'] + 1)
                            # # print 'Found ' + str(state['steps'] + 1)
                            # print state['number']
                            # print nk
                            # print '------'
                            stack.insert(0,{
                                'number': nk,
                                'found': True,
                                'steps': state['steps'] + 1
                            })
                            if state['steps'] < shortest:
                                shortest = state['steps'] + 1
                                # print 'new short ' + str(shortest)
                        else:
                            stateToComapre = {
                                'num': nk,
                                'step': state['steps'] + 1
                            }
                            if notInStateStep(stateToComapre, states):
                                # states.append(nk)
                                stack.append({
                                    'number': nk,
                                    'found': False,
                                    'steps': state['steps'] + 1
                                })
            else:
                stack.insert(0,state)
        # else:
        #     print  len(stack)
            # print stack
    # shortest = 10000000000
    # # print stack
    # for i in stack:
    #     # print i['steps']
    #     if i['steps'] < shortest:
    #         shortest = i['steps']
    return shortest

def flip(pans):
    pans = list(pans)
    pans.reverse()
    newS = ''
    for i in pans:
        if i == '+':
            newS = newS + '-'
        else:
            newS = newS + '+'
    return newS

def countingAlex(s):
    cnt = 0
    prev = s[0]
    for i in range(1,len(s)-1):
        if prev != s[i]:
            prev = s[i]
            cnt += 1
    if prev == '-':
        cnt += 1
    return cnt

def readFile(fileName, fileWrite):
    fw = open(fileWrite, "w")
    fo = open(fileName, "rw+")

    lineNum = int(fo.readline())
    for i in range(0,lineNum):
        start = fo.readline()
        states = []
        print str(start)
        # res= str(counting(start, 0, []))
        res= str(countingAlex(start))
        fw.write('Case #'+str(i+1)+': '+res+'\n')
        print res
        print '#'+str(i+1)
        print '*****************'
        # if i == 3:
        #     quit()

    fo.close()
    fw.close()

readFile('B-large.in', 'result.txt')
