## Template to read file
## Code Jam

with open("input") as fi, open("output","w") as fo:
    count = 0
    case = 0
    for line in fi:
        if count == 0:
            case = line
        else:
            s = line 
            number = []
            d={}
            for i in range(len(s)):
                try: d[s[i]]+=1
                except: d[s[i]]=1
            try:
              if d["Z"]>=1:
                number = number+([0]*d["Z"])
                d["E"] = d["E"]-d["Z"]
                d["R"] = d["R"]-d["Z"]
                d["O"] = d["O"]-d["Z"]
                d["Z"] = 0
            except: pass
            try:
              if d["W"]>=1:
                number = number+([2]*d["W"])
                d["T"] = d["T"]-d["W"]
                d["O"] = d["O"]-d["W"]
                d["W"] = 0
            except: pass
            try:
              if d["U"]>=1:
                number = number+([4]*d["U"])
                d["F"] = d["F"]-d["U"]
                d["R"] = d["R"]-d["U"]
                d["O"] = d["O"]-d["U"]
                d["U"] = 0
            except: pass
            try:
              if d["X"]>=1:
                number = number+([6]*d["X"])
                d["S"] = d["S"]-d["X"]
                d["I"] = d["I"]-d["X"]
                d["X"] = 0
            except: pass
            try:
              if d["G"]>=1:
                number = number+([8]*d["G"])
                d["E"] = d["E"]-d["G"]
                d["I"] = d["I"]-d["G"]
                d["H"] = d["H"]-d["G"]
                d["T"] = d["T"]-d["G"]
                d["G"] = 0 
            except: pass 
            try:
              if d["O"]>=1:
                number = number+([1]*d["O"])
                d["N"] = d["N"]-d["O"]
                d["E"] = d["E"]-d["O"]
                d["O"] = 0
            except: pass
            try:
              if d["F"]>=1:
                number = number+([5]*d["F"])
                d["I"] = d["I"]-d["F"]
                d["V"] = d["V"]-d["F"]
                d["E"] = d["E"]-d["F"]
                d["F"] = 0
            except: pass
            try:
              if d["T"]>=1:
                number = number+([3]*d["T"])
                d["E"] = d["E"]-(d["T"]*2)
                d["R"] = d["R"]-d["T"]
                d["H"] = d["H"]-d["T"]
                d["T"] = 0
            except: pass
            try:
              if d["S"]>=1:
                number = number+([7]*d["S"])
                d["E"] = d["E"]-(d["S"]*2)
                d["V"] = d["V"]-d["S"]
                d["N"] = d["N"]-d["S"]
                d["S"] = 0
            except: pass
            try:
              if d["E"]>=1:
                number = number+([9]*d["E"])
                d["N"] = d["N"]-(d["E"]*2)
                d["I"] = d["I"]-d["E"]
                d["E"] = 0
            except: pass
            number = sorted(number)
            for i in range(len(number)): number[i] = str(number[i])
            number = "".join(number)
            fo.write("Case #"+str(count)+": "+str(number)+"\n")
        count = count + 1
