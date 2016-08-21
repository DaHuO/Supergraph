def main(filename):
    with open(filename) as fin:
        data = fin.read().split()
    cases = int(data[0])
    signs = {'-':False, '+':True}
    with open('out.txt', 'w') as fout:
        for i, line in enumerate(data[1:]):
            
            pancakes = [ signs[c] for c in line]
            sorted_pancakes = False
            steps = 0
            
            while not sorted_pancakes:
                try:
                    end_index = len(pancakes)- pancakes[::-1].index(False)                   
                except:
                    sorted_pancakes = True
                    end_index = 0
                    continue
                           
                leading_pancakes = 0
                while leading_pancakes < end_index and pancakes[leading_pancakes] == pancakes[0]:
                    leading_pancakes+=1
                pancakes = [not p for p in pancakes[:leading_pancakes]][::-1] + pancakes[leading_pancakes:]
                steps += 1

            fout.write("Case #{}: {}\n".format(i+1,steps))
        
       
        


if __name__ == '__main__':
    main('B-large.in')
