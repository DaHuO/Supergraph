import numpy
import sympy
import sys

arr = numpy.array([[1,0,0,0,0,0,0,0,0,0],
                   [1,1,0,2,0,1,0,2,1,1],
                   [1,0,0,1,1,0,0,0,0,0],
                   [1,1,1,0,1,0,0,0,0,0],
                   [0,1,0,0,0,0,0,1,0,2],
                   [0,0,1,1,0,0,0,0,1,0],
                   [0,0,1,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,0,1,0],
                   [0,0,0,0,1,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0,0],
                   [0,0,0,0,0,1,1,0,1,1],
                   [0,0,0,0,0,1,0,1,0,0],
                   [0,0,0,0,0,0,1,1,0,0],
                   [0,0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,1,0]])

n = int(input())

for ix in range(n):
    sinput = input()
    z = [sinput.count('Z')]
    e = [sinput.count('E')]
    r = [sinput.count('R')]
    o = [sinput.count('O')]
    n = [sinput.count('N')]
    t = [sinput.count('T')]
    w = [sinput.count('W')]
    h = [sinput.count('H')]
    f = [sinput.count('F')]
    u = [sinput.count('U')]
    i = [sinput.count('I')]
    v = [sinput.count('V')]
    s = [sinput.count('S')]
    x = [sinput.count('X')]
    g = [sinput.count('G')]
    
    brr = numpy.array([z,e,r,o,n,t,w,h,f,u,i,v,s,x,g])
    arrsolve = numpy.hstack((arr,brr))
    brrsolve = sympy.Matrix(arrsolve).rref()[0].col(-1)
	
    sys.stdout.write('Case #%d: '%(ix+1))
	
    digit = 0
    for row in brrsolve:
	    sys.stdout.write(str(digit) * int(row))
	    digit+=1
    
    sys.stdout.write('\n')
	