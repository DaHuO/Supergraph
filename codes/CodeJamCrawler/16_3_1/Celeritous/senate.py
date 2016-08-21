def problem(inPath, outDir = ""):
    def solve(inPath, processor, outDir = ""):
        from multiprocessing import Pool
        from os import path

        inf = open(inPath, 'rU')
        stem = path.basename(inPath)
        name, extension = path.splitext(stem)
        outName = name + ".out"
        outPath = path.join(outDir, outName)
        outf = open(outPath, 'w')

        inf.readline() #discard the line which tells us how many lines of input there are
        pool = Pool()
        outputs = pool.map(processor, pairs(line.strip() for line in inf))
        for i, result in enumerate(outputs, 1):
            string = "Case #%s: %s" % (i, result)
            if i > 1:
                outf.write("\n")
            outf.write(string)

    solve(inPath, processor, outDir)

def pairs(iterable):
    it = iter(iterable)
    try:
        while True:
            a, b = next(it), next(it)
            yield a, b
    except StopIteration:
        pass

def processor(strings):
    Nstr, Pstr = strings
    Ps = list(map(int, Pstr.split()))
    instructions = " ".join(sub(Ps))
    return instructions

def sub(Ps):
    label = lambda x:chr(ord('A') + x[0])

    while any(P > 0 for P in Ps):
        ordered = sorted(enumerate(Ps), key = lambda x:x[1], reverse = True)
        f, s = ordered[0], ordered[1]
        try:
            t = ordered[2]
        except IndexError:
            t = (None, 0)
        
        labels = label(f)
        Ps[f[0]] -= 1
        if f[1] == s[1] and not t[1] == f[1] == 1:
            Ps[s[0]] -= 1
            yield labels + label(s)
        else:
            yield labels
