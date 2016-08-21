with open("output2.txt", "w") as out:
	with open("teste.txt") as f:
		mais = '+'
		menos = '-'
		l = f.readline()
		for i in range(int(l)):
			line = f.readline().strip()
			linha = []
			for k in line:
				linha.append(k)
			#metrics = [mais]*len(linha)
			flips = 0
			
			while len(linha) != 0:
				if linha[len(linha)-1] == mais:
					#metrics.pop()
					linha.pop()
				elif linha[0] == mais:
					cont = -1
					for j in linha:
						if j == mais:
							cont += 1
						if j == menos:
							break
					flips += 1

					parc = linha[cont::-1]
					for y in range(len(parc)):
						if parc[y] == mais:
							parc[y] = menos
						else:
							parc[y] = mais

					linha = parc+linha[cont+1:len(linha)]
				elif linha[len(linha)-1] == menos:
					flips += 1
					parc = linha[::-1]
				
					for z in range(len(parc)):
						if parc[z] == mais:
							parc[z] = menos
						else:
							parc[z] = mais
					linha = parc

			out.write("Case #{0}: {1} \n".format(i+1,flips))
