#This is the script to synthesize reliability data
#And output it as a file
#Simply call the function generate and specify the number of students

import numpy as np
import matplotlib.pyplot as plt
import math

def generateTestbin(M):
    c = np.random.normal(0.7, 0.2, M)
    c[c > 1] = 1
    c[c < 0] = 0
    return c

def generateTestFix(M):
    c = np.zeros(M)
    for i in range(M):
        if i < math.ceil(M*0.1):
            c[i] = 0.1
        elif i < math.ceil(M*0.3):
            c[i] = 0.5
        elif i < math.ceil(M*0.4):
            c[i] = 0.9
        else:
            c[i] = 0.7
    return c

def generate(M):
    c = generateTestFix(M)

    ## Uncomment the following code if you want to plot the histrogram of the reliability distribution
    '''
    n, bins, patches = plt.hist(c)
    plt.xlabel('Reliability')
    plt.ylabel('Number of student')
    plt.grid(True)
    plt.show()
    '''
    c = np.random.permutation(c)
    f = open('synthesisReliability'+str(M),'w')
    for j in range(M):
        f.write("%.2f\n" % (c[j]))
    f.close()
def main():
    generate(8)
    generate(10)
    generate(50)
    generate(100)
    generate(200)
    generate(500)
    generate(1000)
main()