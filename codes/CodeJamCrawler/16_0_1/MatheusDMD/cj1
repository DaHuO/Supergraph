with open("output2.txt", "w") as out:
	with open("teste.txt") as f:
		l = f.readline()
		for i in range(int(l)):
			pronto = False
			ja_vi = []
			j = 1
			linha = int(f.readline())
			while pronto == False:
				result = linha * j
				if linha == 0:
					out.write("Case #{0}: {1} \n".format(i+1,'INSOMNIA'))
					pronto = True

				pro = result
				for l in range(len(str(result))):
					num = pro%10
					pro = pro//10
					if num not in ja_vi:
						ja_vi.append(num)
				if len(ja_vi) == 10:
					out.write("Case #{0}: {1} \n".format(i+1,result))
					pronto = True
				j += 1