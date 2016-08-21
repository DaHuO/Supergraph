# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 07:53:44 2016

@author: theronrp
"""

f = open('large.in')
fo = open('output.out', 'w')

testCases = int(f.readline())
print testCases

def flip_pancakes (stack, pos):
    tempStack = stack[0:pos+1]
    backwards = pos
    for i in range(0,pos+1):
        if tempStack[backwards] == '+':
            stack[i] = '-'
        elif tempStack[backwards] == '-':
            stack[i] = '+'
        else:
            return
        backwards -= 1
    return stack
    
class pancakeNode:
    def __init__(self, stack, parent, depth):
        self.stack = stack
        self.children = []
        self.parent = parent
        self.depth = depth
        
def smiley_stack(stack):
    result = True
    for element in stack:
        if element == '-':
            result = False
    return result

def makeTree(pancakeNodes, depth):
    pancakeChildren = []    
    for node in pancakeNodes:
        for i in range(0, len(node.stack)):
            childStack = flip_pancakes(node.stack[:], i)
            solutionFound = smiley_stack(childStack)
            if solutionFound:
                #print 'CASE #' + str(i) + ': ' + str(depth)
                #fo.write('CASE #' + str(i) + ': ' + str(depth) + '\n')
                return node
            childNode = pancakeNode(flip_pancakes(node.stack[:], i),node, depth)
            pancakeChildren.append(childNode)            
            node.children.append(childNode)
    #print "number of children :" + str(len(pancakeChildren)) 
    solutionNode = makeTree(pancakeChildren, depth + 1)
    return solutionNode
    
def findMinFlips(stack, goal):
    if len(stack) == 0:
        return 0
    bottomPancake = stack[len(stack) - 1]
    trailingEdgeLength = 1
    for i in range(1,len(stack)):
        if stack[len(stack) - 1 - i] == bottomPancake:
            trailingEdgeLength += 1
        else:
            break
    #print trailingEdgeLength
    subStack = stack[0:len(stack) - trailingEdgeLength]
    if bottomPancake == goal:
        return findMinFlips(subStack, bottomPancake)        
    elif bottomPancake != goal:
        return findMinFlips(subStack, bottomPancake) + 1
        

for i in range(0,testCases):
    inputLine = str(f.readline())
    pancakeStack = list(inputLine.rstrip('\n'))
    #pancakeStack = list('--+--++')
    print 'CASE #' + str(i + 1) + ': ' + str(findMinFlips(pancakeStack, '+'))
    fo.write('CASE #' + str(i + 1) + ': ' + str(findMinFlips(pancakeStack, '+')) + '\n')
    """if smiley_stack(pancakeStack):
        print 'CASE #' + str(i+1) + ': ' + str(0)
        fo.write('CASE #' + str(i+1) + ': ' + str(0) + '\n')
    else:
        pancakeRoot = pancakeNode(pancakeStack, -1, 0)
        solutionNode = makeTree([pancakeRoot], 1)
        print 'CASE #' + str(i + 1) + '(method2): ' + str(solutionNode.depth + 1)
        donePrinting = False
        if solutionNode.parent == -1:
            print str(solutionNode.stack)
            donePrinting = True
        while not donePrinting:
            print str(solutionNode.stack)
            solutionNode = solutionNode.parent
            if solutionNode.parent == -1:
                print str(solutionNode.stack)
                donePrinting = True"""
            
f.close()
fo.close()
#returnStack = flip_pancakes(testStack[:], 3)
#flip_pancakes(testStack, 0)
#flip_pancakes(testStack, 1)
        