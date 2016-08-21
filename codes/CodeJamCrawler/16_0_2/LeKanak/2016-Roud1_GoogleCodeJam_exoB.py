""" Google Code Jam 2016 - Part B

"""


def ThePancakeRevenge(pancakes):
    """ Return the number of change in the Stack of Pancakes """
    cnt = sum(map(lambda i: pancakes[i] != pancakes[i+1], range(len(pancakes)-1)))
    return cnt + (pancakes[0]=='-' and (cnt%2)==0) + (pancakes[0]=='+' and (cnt%2)==1)

"""
Part to be executed with the given input files

"""

path = r'C:\Users\HOME\Desktop\GoogleCodeJam'
fileName = 'B-large.in'
inputPath = r'%s\%s' % (path, fileName)
outputPath = r'%s\%s' % (path, fileName.replace('.in', '_out.dat'))

caseNb = None
outputFile = open(outputPath, 'w')
for i, line in enumerate(open(inputPath, 'r')):
    if not caseNb:
        caseNb = int(line)
        continue

    outputFile.write('Case #%s: %s\n' % (i, ThePancakeRevenge(line.strip())))
outputFile.close()