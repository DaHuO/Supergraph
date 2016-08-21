from __future__ import print_function

def sheep(input_file, output_file):
    with open(input_file) as input_f:
        with open(output_file, 'w') as output_f: 
            n = input_f.readline().strip()
            mas = input_f.read().split('\n')
            mas = [int(elem) for elem in mas]
            num_set = set()
            for pos, num in enumerate(mas):
                elems_in_num = [int(i) for i in str(num)]
                num_set.update(elems_in_num)
                if num_set == set([0,1,2,3,4,5,6,7,8,9]):
                    result = num
                    print("Case #{}: ".format(pos+1) + str(result),
                          file=output_f)
                    num_set.clear()
                    continue
                else:
                    for i in range(1,1000):
                        num_ = num * i
                        elems_in_num = [int(i) for i in str(num_)]
                        num_set.update(elems_in_num)
                        result = 'INSOMNIA'
                        if num_set == set([0,1,2,3,4,5,6,7,8,9]):
                            result = num_
                            print("Case #{}: ".format(pos+1) + str(result),
                                  file=output_f)
                            num_set.clear()
                            break
                        else:
                            pass
                    if result == 'INSOMNIA':
                        print("Case #{}: ".format(pos+1) + str(result),
                              file=output_f)
                        num_set.clear()
            
                    
                
            
            
            
            

