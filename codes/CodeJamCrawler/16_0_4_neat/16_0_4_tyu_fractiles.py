input_file = "D-small-attempt0.in"
output_file = "D-small-attempt0.out"

def main():
    results = []
    
    f = open(input_file, 'r')
    T = int(f.readline())
    for t in range(T):
        K,C,S = f.readline().split()
        tiles = find_gold(int(K),int(C), int(S))
        results.append(tiles)
    f.close()

    f_out = open(output_file, 'w')
    for t in range(T):
        f_out.write('Case #%d:%s\n' % (t+1, results[t]))
    f_out.close()

#Small dataset: assume K=S
def find_gold(K,C,S):
    tiles = ""
    for i in range(K):
        tiles = tiles + (' %d' % (i+1))
    return tiles

if __name__ == "__main__":
    main()
