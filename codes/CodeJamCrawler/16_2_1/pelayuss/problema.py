T=int(raw_input())
for I in xrange(1, T+1):
	cad=str(raw_input())
	arreglo=[]
	tam=len(cad)
	##print cad[0:1]+cad[2:]
	while 'Z' in cad:  ##zero
		arreglo.append( 0 )
		pos=cad.index('Z')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('R')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('O')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
	##print cad
	while 'W' in cad:  ##dos
		arreglo.append( 2 )
		pos=cad.index('T')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('W')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('O')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
	while 'U' in cad:  ##4
		arreglo.append( 4 )
		pos=cad.index('F')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('O')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('U')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('R')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
	while 'G' in cad:  ##8
		arreglo.append( 8 )
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('I')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('G')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('H')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('T')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
	while 'X' in cad:  ##6
		arreglo.append( 6 )
		pos=cad.index('S')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('I')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('X')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
	while 'T' in cad:  ##3
		arreglo.append( 3 )
		pos=cad.index('T')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('H')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('R')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
	while 'F' in cad:  ##5
		arreglo.append( 5 )
		pos=cad.index('F')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('I')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('V')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
	while 'V' in cad:  ##7
		arreglo.append( 7 )
		pos=cad.index('S')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('V')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('N')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
	while 'O' in cad:  ##1
		arreglo.append( 1 )
		pos=cad.index('O')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('N')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
	while 'N' in cad:  ##9
		arreglo.append( 9 )
		pos=cad.index('N')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('I')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('N')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
		pos=cad.index('E')
		cadi=cad[0:pos]
		cadi2=cad[pos+1:]
		cad=cadi+cadi2
		
	impri="Case #"+str(I)+": "
	arreglo.sort()
	for j in xrange(0, len(arreglo)):
		impri=impri+str( arreglo[j ] )
	print impri
