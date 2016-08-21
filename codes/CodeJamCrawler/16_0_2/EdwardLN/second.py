from __future__ import print_function

def pancake(input_file, output_file):
    with open(input_file) as input_f:
        with open(output_file, 'w') as output_f:
            n = input_f.readline().strip()
            mas = input_f.read().split('\n')
            for i, sequence in enumerate(mas):
                iter_ = 0
                if '-' not in sequence:
                    print('Case #{}: {}'.format(i+1, 0), file=output_f)
                    continue
                if '+' not in sequence:
                    print('Case #{}: {}'.format(i+1, 1), file=output_f)
                    continue
                while True:
                    if sequence[0] == '-':
                        if '+' not in sequence:
                            print('Case #{}: {}'.format(i+1, iter_+1), file=output_f)
                            break
                        else:
                            plus_pos = sequence.find('+')
                            sequence = sequence.replace(sequence[:plus_pos+1], '+' * (plus_pos+1), 1)
                            iter_ += 1
                    elif sequence[0] == '+':
                        if '-' not in sequence:
                            print('Case #{}: {}'.format(i+1, iter_), file=output_f)
                            break
                        else:
                            minus_pos = sequence.find('-')
                            sequence = sequence.replace(sequence[:minus_pos+1], '-' * (minus_pos+1), 1)
                            iter_ += 1
                    
                    
                
