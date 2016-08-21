
def generate_org_artwork(K):
    for i in xrange(K):
        base = ['L'] * K
        base[i] = 'G'
        yield base

def develop(artwork, complexity):
    """
    Develop artwork based on complexity
    :param artwork: base artwork
    :param complexity:
    :return: modified artwork
    """
    if complexity == 1:
        return artwork
    out = []
    for i in range(1,complexity):
        for s in artwork:
            if s=='L':
                out.extend(artwork)
            else:
                out.extend(['G']*len(artwork))
    return out

def find_most_frequent_piece( artworks ):
    """
    Find the most frequenct artwork with 'G'
    :param artworks: list of artworks
    :return:
    """
    max_frequency= 0
    max_id =0
    for i in xrange(len(artworks[0])):
        freq = 0
        for g in artworks:
            if g[i] == 'G':
                freq+=1
        if freq > max_frequency:
            max_frequency = freq
            max_id = i
    return max_id

def eleminate_artwork( gid , artworks):
    """
    Remove all artwork the has in the gid
    :param gid: the piece idx in artworks
    :param artworks: list of possible artworks
    :return:
    """
    i=0
    while i < len(artworks):
        if artworks[i][gid] == 'G':
            artworks.pop(i)
        else:
            i+=1


def solve(K,C,S):
    """
    Solve for given K,C,S
    :param K: Base length
    :param C: Complexity
    :param S: Allowed number of hiring
    :return:
    """
    artwork_gen = generate_org_artwork( K )
    ids=[]
    artworks = [develop(a,C) for a in artwork_gen]
    while len(artworks) > 0:
        gid = find_most_frequent_piece( artworks )
        eleminate_artwork( gid, artworks)
        ids.append(str(gid+1))
    return ids


T=int(raw_input())
for i in xrange(T):
    K,C,S = (int(n) for n in raw_input().split(' '))
    s = solve(K,C,S)
    res = ' '.join(s) if len(s)<=S else "IMPOSSIBLE"
    print("Case #%d: %s"%(i+1,res))