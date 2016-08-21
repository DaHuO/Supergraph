import string
stevke = [str(i) for i  in range(0,10)] + [i for i in string.ascii_uppercase]
#print stevke
def Pretvori(stevilo, sistemZac, sistemKonc):
	#stevilo more biti string, sistema pa int
	deset = int(stevilo,sistemZac)
	st = []
	#evklidov algoritem da dobim vse stevke v obratnem vrstnem redu
	while (deset//sistemKonc !=0):
		st.append(stevke[deset%sistemKonc])
		deset //= sistemKonc
	#ker prej koncam se zadnjo stevke appedam v array
	st.append(stevke[deset])
	return "".join(st[::-1])

def isPrastevilo(x):
	i = 2
	while(i*i <= x):
		if(x % i == 0):
			return False
		
		i += 1

	return True

prastevila = []


t = int(raw_input())

for i in range(t):
	n, j = map(int,raw_input().split())

	print "Case #{0}:".format(i+1)
	for biti in range(2**n):
		fl = True
		nonTrivialDiv = []
		biti = "{0:b}".format(biti)
		
		if(len(biti) < n or biti[0] == "0" or biti[-1] == "0"):
			continue

		#print "moznost: " + biti
		for k in range(2,11):
			stevSistem = int(Pretvori(biti, k, 10))
			
			if(stevSistem in prastevila or isPrastevilo(stevSistem)):
				fl = False
				break

			l = 2
			#print "sistem " + str(k) + " :" + str(stevSistem)
			while (l*l <= stevSistem):
				if(stevSistem % l == 0):
					nonTrivialDiv.append(l)
					break

				l+=1

		if(not fl): continue
		j -= 1
		print "{0} {1}".format(biti, " ".join(map(str,nonTrivialDiv)))
		if(j <= 0):
			break

