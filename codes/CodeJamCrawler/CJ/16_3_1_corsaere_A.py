INPUT_FILE = "A-large.in"
OUTPUT_FILE = "A-large.out"
with open(INPUT_FILE) as f:
    with open(OUTPUT_FILE, "w") as of:
        cases = int(f.readline())
        for case in range(cases):
            num_letters = int(f.readline())
            layout = map(int, f.readline().strip().split())
            heap = []
            total = 0
            for x in range(len(layout)):
                total += layout[x]
                heap.append((layout[x], x))
            heap = sorted(heap)
            
            evac_plan = []
            while heap:
                evac_statement = ""
                majority, index = heap.pop() # layout[x], x
                minority = total - majority
                if minority == majority + 1:
                    evac_statement += chr(ord('A') + index)
                    if majority - 1 > 0:
                        heap.append((majority-1, index))
                    total = total - 1
                elif minority >= majority + 2:
                    mval, mindex = heap.pop()
                    evac_statement += chr(ord('A') + mindex)
                    if mval > 1:
                        evac_statement += chr(ord('A') + mindex)
                        if mval - 2 > 0:
                            heap.append((mval-2, mindex))
                    else:
                        mval, mindex = heap.pop()
                        evac_statement += chr(ord('A') + mindex)
                        if mval - 1 > 0:
                            heap.append((mval-1, mindex))
                    heap.append((majority, index))
                    total = total - 2
                else:
                    mval, mindex = heap.pop()
                    evac_statement += chr(ord('A') + index)
                    evac_statement  += chr(ord('A') + mindex)
                    if mval - 1 > 0:
                        heap.append((mval-1, mindex))
                    if majority - 1 > 0:
                        heap.append((majority-1, index))
                    total = total - 2
                heap = sorted(heap)
                evac_plan.append(evac_statement)
            of.write("Case #{0}: {1}".format(case+1, " ".join(evac_plan)))
            of.write("\n")
