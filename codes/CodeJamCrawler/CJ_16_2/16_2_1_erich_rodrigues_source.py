n = int(raw_input())
i = 1
while i <= n:
    resposta = ""
    entrada = sorted(raw_input())
    while 'Z' in entrada and 'E' in entrada and 'R' in entrada and 'O' in entrada:
	entrada.remove('Z')
	entrada.remove('E')
	entrada.remove('R')
	entrada.remove('O')
	resposta += "0"

    while 'T' in entrada and 'W' in entrada and 'O' in entrada:
	entrada.remove('T')
	entrada.remove('W')
	entrada.remove('O')
	resposta += "2"
    while 'S' in entrada and 'I' in entrada and 'X' in entrada:
	entrada.remove('S')
	entrada.remove('I')
	entrada.remove('X')
	resposta += "6"
    while 'E' in entrada and 'I' in entrada and 'G' in entrada and 'T' in entrada and 'H' in entrada:
	entrada.remove('E')
	entrada.remove('I')
	entrada.remove('G')
	entrada.remove('H')
	entrada.remove('T')
	resposta += "8"
    while 'F' in entrada and 'O' in entrada and 'U' in entrada and 'R' in entrada:
	entrada.remove('F')
	entrada.remove('O')
	entrada.remove('U')
	entrada.remove('R')
	resposta += "4"
    while 'F' in entrada and 'I' in entrada and 'V' in entrada and 'E' in entrada:
	entrada.remove('F')
	entrada.remove('I')
	entrada.remove('V')
	entrada.remove('E')
	resposta += "5"
    while 'S' in entrada and 'E' in entrada and 'V' in entrada and 'E' in entrada and 'N' in entrada:
	entrada.remove('S')
	entrada.remove('E')
	entrada.remove('V')
	entrada.remove('E')
	entrada.remove('N')
	resposta += "7"
    while 'O' in entrada and 'N' in entrada and 'E' in entrada:
	entrada.remove('O')
	entrada.remove('N')
	entrada.remove('E')
	resposta += "1"
   
    while 'T' in entrada and 'H' in entrada and 'R' in entrada and entrada.count('E') >= 2:
	entrada.remove('T')
	entrada.remove('H')
	entrada.remove('R')
	entrada.remove('E')
	entrada.remove('E')
	resposta += "3"
    while 'N' in entrada and 'I' in entrada and 'N' in entrada and 'E' in entrada:
	entrada.remove('N')
	entrada.remove('I')
	entrada.remove('N')
	entrada.remove('E')
	resposta += "9"

    print "Case #" + str(i) + ": " + ''.join(sorted(resposta))
    i += 1
